#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/29 18:41
=================================================="""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger


class MainPage:

    def __init__(self):
        login_page = LoginPage()  # 创建一个页面对象
        login_page.input_username('test')
        login_page.input_password('newdream123')
        login_page.click_login()
        self.driver = login_page.driver   # 把login的driver转移到main_page
        self.companyname_showbox = self.driver.find_element(By.ID, 'companyname')
        self.myzone_menu = self.driver.find_element(By.XPATH, '//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//li[@data-id="product"]')
        self.user_showbox = self.driver.find_element(By.CLASS_NAME, 'user-name')

    def get_companyname(self):   # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        logger.info('获取到公司名称 [%s]' % value)
        return value

    def goto_myzone(self):   # 选择我的地盘
        self.myzone_menu.click()
        logger.info('进入到我的地盘')

    def goto_product(self):
        self.product_menu.click()
        logger.info('点击产品按钮')

    def get_username(self):
        value = self.user_showbox.text
        logger.info('获取到用户名 [%s]' % value)
        return value


if __name__ == '__main__':
    main_page = MainPage()
    main_page.goto_myzone()
    main_page.goto_product()
    username = main_page.get_username()
    print(username)