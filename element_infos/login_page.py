#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/29 18:01
=================================================="""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger


current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')


class LoginPage:

    def __init__(self):
        # 创建logger对象
        logger.info('UI自动化测试')
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=loginz')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        logger.info('打开了网页：[%s]' % self.driver.current_url)
        self.username_inputbox = self.driver.find_element(By.NAME, 'account')    # 属性———> 控件
        self.password_inputbox = self.driver.find_element(By.NAME, 'password')
        self.login_button = self.driver.find_element(By.ID, 'submit')
        self.keeploginon_checkbox = self.driver.find_element(By.ID, 'keepLoginon')

    def input_username(self, username):  # 方法：控件的操作
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：' + str(username))

    def input_password(self, password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：' + str(password))

    def click_login(self):
        self.login_button.click()
        logger.info('点击登录按钮')


if __name__ == '__main__':
    login_page = LoginPage()   # 创建一个页面对象
    login_page.input_username('test')
    login_page.input_password('newdream123')
    # print(type(login_page.driver.current_url))
    login_page.click_login()
    time.sleep(5)
    login_page.driver.quit()
