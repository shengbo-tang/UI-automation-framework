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
from common.test_data_utils import TestDataUtils


class LoginCase(SeleniumBaseCase):

    def setUp(self) -> None:
        super().setUp()     # 继承SeleniumBaseCase类的setup
        # print(''LoginCase测试类的初始化)     # 个性化的前置条件
        # 整个测试类的测试数据
        self.test_class_data = TestDataUtils('login_suite', 'LoginCase').convert_exceldata_to_testdata()

    def test_login_success(self):
        test_function_data = self.test_class_data['test_login_success']     # 当前测试方法数据
        self._testMethodDoc = test_function_data['test_name']       # 测试用例备注
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),
                                               test_function_data['test_parameter'].get('password'))
        main_page.wait(2)
        # 断言
        # self.assertEqual('测试人员1', '测试人员1', '提示：登录失败')
        self.assertEqual(main_page.get_username(), test_function_data['excepted_result'], '提示：登录失败')

    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']  # 当前测试方法数据
        self._testMethodDoc = test_function_data['test_name']       # 测试用例备注
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),
                                                test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result, test_function_data['excepted_result'])


if __name__ == '__main__':
    unittest.main()
