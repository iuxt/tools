import os, re
from readline import insert_text
import sqlite3

sqlite_file = "/tmp/freeradius.db"

def insert_userlist(password_dict):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    if password_dict:
        c.execute("DELETE FROM radcheck")
        c.execute("DELETE FROM sqlite_sequence")
        for k,v in password_dict.items():
            c.execute("INSERT OR REPLACE INTO radcheck (username, attribute, op, value) \
                    VALUES ('%s','Cleartext-Password',':=','%s')" % (k,v))
        conn.commit()
        conn.close()
    else:
        print("字典为空")


def get_password(username):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    cursor = c.execute("SELECT value from radcheck WHERE username = '%s'" % username)
    for row in cursor:
        return row[0]

    print ("数据操作成功")
    conn.close()


def insert_user(k, v):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO radcheck (username, attribute, op, value) \
                VALUES ('%s','Cleartext-Password',':=','%s')" % (k,v))
    conn.commit()
    print("增加用户成功")
    conn.close()


if __name__ == '__main__':
    insert_userlist({'zhanglikun':'test1', 'zhangsan':'test1'})
    insert_user("zhanglikun", 'test4')
    print(get_password('zhanglikun'), get_password('zhangsan'))
    # print(config_list)