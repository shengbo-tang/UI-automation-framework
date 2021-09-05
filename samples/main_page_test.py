#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 22:38
=================================================="""
from common.browser import Browser
from common.config_utils import local_config
from actions.login_action import LoginAction


driver = Browser().get_driver()
driver.get(local_config.get_url)
driver.maximize_window()
main_page = LoginAction(driver).default_login()
value = main_page.get_username()
main_page.wait(5)
print(value)
