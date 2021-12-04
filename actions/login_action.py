#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 19:07
=================================================="""
# 登录页面的功能操作
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import local_config


class LoginAction:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    # 提取公共的登录操作
    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    # 操作1：登录成功
    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login_page.driver)   # 如果登录成功，返回一个主页面

    # 操作2：登录失败
    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    # 操作3：默认登录
    def default_login(self):
        self.login_success(local_config.user_name, local_config.pass_word)
        return MainPage(self.login_page.driver)    # 如果登录成功，返回一个主页面

    # 操作4：cookie
    def login_by_cookie(self):
        pass

