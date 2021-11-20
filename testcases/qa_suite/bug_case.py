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


class CommitBug(SeleniumBaseCase):

    def test_commit_bug(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()

        commit_bug_action = CommitBugAction(main_page.driver)
        main_page = commit_bug_action.commit_bug('唐同学的11-20号', '好好学习，天天向上')
        main_page.wait(3)
        actual_result = main_page.get_title()
        self.assertEqual(actual_result.__contains__('DBShop电商项目::Bug - 禅道'), True, '提交Bug失败')


if __name__ == '__main__':
    unittest.main()
