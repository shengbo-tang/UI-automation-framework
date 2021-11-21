#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/5 22:19
=================================================="""
import unittest
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class QuitCase(SeleniumBaseCase):

    def setUp(self) -> None:
        super().setUp()
        self.test_class_data = TestDataUtils('main_suite', 'QuitTest').convert_exceldata_to_testdata()

    def test_quit(self):
        test_function_data = self.test_class_data['test_quit']
        self._testMethodDoc = test_function_data['test_name']  # 测试用例备注
        login_action = LoginAction(self.base_page.driver)   # 登录的动作对象
        main_page = login_action.default_login()   # 默认登录之后返回主页面
        quit_action = QuitAction(main_page.driver)   # 提出动作对象
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']),
                         True, '提示：test_quit用例不通过')


if __name__ == '__main__':
    unittest.main()
