import random,string
import os


src = string.ascii_letters + string.digits
list_passwd_all = random.sample(src, 12) #从字母和数字中随机取12位
list_passwd_all.extend(random.sample(string.digits, 1))  #让密码中一定包含数字
list_passwd_all.extend(random.sample(string.ascii_lowercase, 1)) #让密码中一定包含小写字母
list_passwd_all.extend(random.sample(string.ascii_uppercase, 1)) #让密码中一定包含大写字母
# list_passwd_all.extend(random.sample(string.punctuation, 2)) #让密码中一定包含字符
random.shuffle(list_passwd_all) #打乱列表顺序
str_passwd = ''.join(list_passwd_all) #将列表转化为字符串


os.system(r'echo|set /p=%s| clip' % str_passwd) # 将字符串写入剪贴板

# 生成随机密码的工具， windows系统使用会自动复制到剪贴板