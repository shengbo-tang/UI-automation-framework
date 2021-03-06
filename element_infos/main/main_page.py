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
from common.element_data_utils import ElementDataUtils
from common.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']

    def goto_myzone(self):
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    # 点击用户菜单
    def click_username(self):
        self.click(self.user_menu)

    # 点击退出按钮
    def click_quit_button(self):
        self.click(self.quit_button)

