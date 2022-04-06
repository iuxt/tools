from hashlib import md5
import dotenv
from os import getenv

dotenv.load_dotenv()

def get_password(username):
    md5_obj = md5()
    salt = getenv('SALT')
    md5_obj.update(username.encode('utf-8') + salt.encode('utf-8'))
    return md5_obj.hexdigest()[:12]
    

if __name__ == '__main__':
    print(get_password('zhanglikun'))
