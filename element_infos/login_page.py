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
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')


class LoginPage(BasePage):

    def __init__(self, driver):
        # driver的处理  子类的构造方法需要显示调用父类
        # 方法一：
        super().__init__(driver)
        # 方法二：
        # BasePage.__init__(self, driver)
        element = ElementDataUtils('login_page').get_element_info()
        self.username_inputbox = element['username_inputbox']
        self.password_inputbox = element['password_inputbox']
        self.login_button = element['login_button']

    def input_username(self, username):  # 方法：控件的操作
        self.input(self.username_inputbox, username)
        logger.info('用户名输入框输入：' + str(username))

    def input_password(self, password):
        self.input(self.password_inputbox, password)
        logger.info('密码输入框输入：' + str(password))

    def click_login(self):
        self.click(self.login_button)
        logger.info('点击登录按钮')


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=loginz')
    login_page.set_browser_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()


