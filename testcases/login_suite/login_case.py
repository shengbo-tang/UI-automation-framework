#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 21:54
=================================================="""
import unittest
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase


class LoginCase(SeleniumBaseCase):

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('test01', 'newdream123')
        main_page.wait(2)
        # 断言
        # self.assertEqual('测试人员1', '测试人员1', '提示：登录失败')
        self.assertEqual(main_page.get_username(), '测试人员1', '提示：登录失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('test01', 'newdream')
        print(actual_result)
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。')


if __name__ == '__main__':
    unittest.main()
