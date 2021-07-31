# 这个脚本是重置beyondcompare试用的脚本，就是可以实现一直试用。
import os
import getpass

username = getpass.getuser()

def get_sid():
    output = os.popen("whoami /user").readlines()
    for line in output:
        if username in line:
            sid = line.split(" ")[-1].strip("\n")
    return sid


def delete_bc_trial_information():
    sid = get_sid()
    result = os.popen("reg delete \"HKEY_USERS\%s\Software\Scooter Software\Beyond Compare 4\" /v CacheId /f" % sid)
    return result

if __name__ == '__main__':
    print(delete_bc_trial_information())
    os.system("pause")
