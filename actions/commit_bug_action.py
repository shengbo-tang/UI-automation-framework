#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 21:39
=================================================="""
# 提交bug动作类
from element_infos.bug.bug_page import BugPage
from element_infos.main.main_page import MainPage


class CommitBugAction:

    def __init__(self, driver):
        self.commit_bug_page = BugPage(driver)

    def commit_bug(self, bug_title, bug_content):
        self.commit_bug_page.click_qa()
        self.commit_bug_page.click_bug()
        self.commit_bug_page.click_create_bug()
        # 选择所属模块
        self.commit_bug_page.click_bug_module_select()
        self.commit_bug_page.click_bug_module_choose()
        # 选择所属项目
        self.commit_bug_page.click_bug_project_select()
        self.commit_bug_page.click_bug_project_choose()
        # 选择影响版本
        self.commit_bug_page.double_click_bug_version_select()
        self.commit_bug_page.click_bug_version_choose()
        # 选择截止日期
        self.commit_bug_page.click_bug_datetime_select()
        self.commit_bug_page.click_bug_datetime_choose()
        # 选择操作系统
        self.commit_bug_page.click_bug_system_select()
        self.commit_bug_page.click_bug_system_choose()
        # 选择浏览器
        self.commit_bug_page.click_bug_browser_select()
        self.commit_bug_page.click_bug_browser_choose()
        # 输入bug标题
        self.commit_bug_page.input_bug_title(bug_title)
        # 切换到bug步骤框架
        self.commit_bug_page.click_bug_steps_frame()
        # 输入bug步骤
        self.commit_bug_page.input_bug_steps(bug_content)
        # 回到默认框架
        self.commit_bug_page.switch_to_default_frame()
        # 保存按钮
        self.commit_bug_page.click_bug_save_button()
        return MainPage(self.commit_bug_page.driver)
