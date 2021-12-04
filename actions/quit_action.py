#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 23:11
=================================================="""
# 退出的动作类
from element_infos.main.main_page import MainPage
from element_infos.login.login_page import LoginPage


class QuitAction:

    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)  # 退出后返回一个主页面

