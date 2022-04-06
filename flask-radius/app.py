import os
from flask import Flask, render_template, request, session
import requests
import dotenv
import _team_request
import generate_password
import freeradius_user

app = Flask(__name__)
dotenv.load_dotenv()
app.secret_key = os.getenv("SECRET_KEY", "not set key")

# 定时命令，用于更新用户列表，主要是删除用户的更新
@app.cli.command()
def update_userdict():
    userdict = {}
    content = requests.get(os.getenv('nutstore_user_url'), auth=(os.getenv('nutstore_admin_username'), os.getenv('nutstore_admin_password'))).content
    for i in _team_request.parse_team_members(content):
        useremail = i['user_name']
        if useremail != None:
            username = useremail[:useremail.index('@')]
            password = generate_password.get_password(username)
            userdict[username] = password
    freeradius_user.insert_userlist(userdict)

@app.route('/')
def index():
    email = request.headers.get("X-pomerium-Claim-Email", None)
    # email = 'zhanglikun@nutstore.net'
    username = email[:email.index('@')]
    password = freeradius_user.get_password(username)
    if not password:
        password = generate_password.get_password(username)
        freeradius_user.insert_user(username, password)

    return render_template('index.html', username=username, password=password)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
