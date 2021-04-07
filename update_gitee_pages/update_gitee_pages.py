#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

conf = configparser.ConfigParser()
conf.read('config')
username = conf['user']['username']
password = conf['user']['password']

# 模拟浏览器打开到gitee登录界面
driver = webdriver.Chrome()
driver.get('https://gitee.com/login')
# 将窗口最大化
driver.maximize_window()
time.sleep(2)

# 输入账号--通过html的id属性定位输入位置--改为你的账号
driver.find_element_by_id('user_login').send_keys(username)
# 输入密码--通过html的id属性定位输入位置--改为你的密码
driver.find_element_by_id('user_password').send_keys(password)
# 点击登录按钮--通过xpath确定点击位置
driver.find_element_by_xpath(
    '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/form[1]/div[2]/div/div/div[4]/input').click()

time.sleep(2)

# 切换到gitee pages界面--改为you_gitee_id
driver.get('https://gitee.com/iuxt/iuxt/pages')
# 点击更新按钮--通过xpath确定点击位置
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/form/div[7]').click()
# 确认更新提示框--这个函数的作用是确认提示框
Alert(driver).accept()

# 等待5秒更新
time.sleep(5)

# 脚本运行成功,退出浏览器
driver.quit()
