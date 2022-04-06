import pyautogui
import time
import os
import sys
import pyperclip
import configparser

config=configparser.ConfigParser()
config.read('config.ini')
app = sys.argv[1]

def findFile(base):
    g = os.walk(base)
    for path,dir_list,file_list in g:
        for f in file_list:
            fullname = os.path.join(path, f)
            yield fullname

def findPhprFilename(base):
    for i in findFile(base):
        if ".phpr" in i:
            return i

os.system('start %s' % findPhprFilename(config[app]['phpr_location']))


# 点击run按钮
while True:
    run_location = pyautogui.locateCenterOnScreen('img\\win11\\run.png')
    if run_location:
        break
    else:
        time.sleep(2)
        print("wait for run")
pyautogui.click(run_location)


# 点击output
while True:
    output_location = pyautogui.locateCenterOnScreen('img\\win11\\output.png')
    if output_location:
        break
    else:
        time.sleep(2)
        print("wait for output")
pyautogui.click(output_location)


# 设置导出路径
while True:
    browse_location = pyautogui.locateCenterOnScreen('img\\win11\\browse.png')
    if browse_location:
        print(browse_location)
        folder_location = (browse_location[0] - 200 , browse_location[1])
        print(folder_location)
        break
    else:
        time.sleep(2)
        print("wait for browse")
pyautogui.click(folder_location)
pyperclip.copy(config[app]['output_folder'])
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')


# 点击NEW
while True:
    new_location = pyautogui.locateCenterOnScreen('img\\win11\\new.png')
    if new_location:
        break
    else:
        time.sleep(2)
        print("wait for new")
pyautogui.click(new_location)


# 修改数据库配置
while True:
    ok_location = pyautogui.locateCenterOnScreen('img\\win11\\ok.png')
    if ok_location:
        database_location = (ok_location[0] , ok_location[1] - 200 )
        break
    else:
        time.sleep(2)
        print("wait for ok location")
pyautogui.click(database_location)
pyperclip.copy(config[app]['database_config'])
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui.click(ok_location)


# 点击build
while True:
    build_location = pyautogui.locateCenterOnScreen('img\\win11\\build.png')
    if build_location:
        break
    else:
        time.sleep(2)
        print("wait for build")
pyautogui.click(build_location)


# 等待build完成,点击close
while True:
    build_success = pyautogui.locateCenterOnScreen('img\\win11\\build_success.png')
    if build_success:
        break
    else:
        time.sleep(2)
        print("wait for build success")
close_location = pyautogui.locateCenterOnScreen('img\\win11\\close.png')
pyautogui.click(close_location)


# 点击no
while True:
    no_location = pyautogui.locateCenterOnScreen('img\\win11\\no.png')
    if no_location:
        break
    else:
        time.sleep(2)
        print("wait for no")
pyautogui.click(no_location)