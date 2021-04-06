import os

pipfolder = os.getenv("USERPROFILE") + "\pip"
pipfile = pipfolder + "\pip.ini"
print(pipfolder)
print(pipfile)

if not os.path.exists(pipfolder):
    print("开始创建pip文件夹")
    os.mkdir(pipfolder)
else:
    print("pip 文件夹存在")

if not os.path.exists(pipfile):
    print("开始生成pip.ini文件")
    with open(pipfile , "w+") as cf:
        cf.writelines("[global]\ntimeout = 6000\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple\ntrusted-host = pypi.tuna.tsinghua.edu.cn")
else:
    print("pip.ini 文件已存在，忽略")


os.system("pause")