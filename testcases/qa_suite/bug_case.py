#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：11/18/21 18:01
=================================================="""
import time
import unittest
from common.selenium_base_case import SeleniumBaseCase
from actions.commit_bug_action import CommitBugAction
from actions.login_action import LoginAction
from common.test_data_utils import TestDataUtils


class CommitBug(SeleniumBaseCase):

    test_class_data = TestDataUtils('test_suite', 'creat_bug_case', 'CommitbugTest').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()

    @unittest.skipIf(test_class_data['commit_bug']['is_not'], '条件为真跳过')
    def test_commit_bug(self):
        test_function_data = self.test_class_data['commit_bug']
        self._testMethodDoc = test_function_data['test_name'] + str(test_function_data['is_not'])  # 测试用例备注
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()

        commit_bug_action = CommitBugAction(main_page.driver)
        main_page = commit_bug_action.commit_bug(test_function_data['test_parameter'].get('bug_title'),
                                                 test_function_data['test_parameter'].get('bug_content'))
        main_page.wait(3)
        actual_result = main_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, '提交Bug失败')


if __name__ == '__main__':
    unittest.main()
