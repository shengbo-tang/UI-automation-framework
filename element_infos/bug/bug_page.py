#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：11/18/21 16:47
=================================================="""
from common.element_data_utils import ElementDataUtils
from common.base_page import BasePage


class BugPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element = ElementDataUtils('bug', 'bug_page').get_element_info()
        self.qa_click = element['qa_click']
        self.bug_click = element['bug_click']
        self.create_bug_button = element['create_bug_button']
        self.bug_module_select = element['bug_module_select']
        self.bug_module_choose = element['bug_module_choose']
        self.bug_project_select = element['bug_project_select']
        self.bug_project_choose = element['bug_project_choose']
        self.bug_version_select = element['bug_version_select']
        self.bug_version_choose = element['bug_version_choose']
        self.bug_datetime_select = element['bug_datetime_select']
        self.bug_datetime_choose = element['bug_datetime_choose']
        self.bug_system_select = element['bug_system_select']
        self.bug_system_choose = element['bug_system_choose']
        self.bug_browser_select = element['bug_browser_select']
        self.bug_browser_choose = element['bug_browser_choose']
        self.bug_title_input = element['bug_title_input']
        self.bug_steps_frame = element['bug_steps_frame']
        self.bug_steps_input = element['bug_steps_input']
        self.bug_save_button = element['bug_save_button']

    def click_qa(self):
        self.click(self.qa_click)

    def click_bug(self):
        self.click(self.bug_click)

    def click_create_bug(self):
        self.click(self.create_bug_button)

    def click_bug_module_select(self):
        self.click(self.bug_module_select)

    def click_bug_module_choose(self):
        self.click(self.bug_module_choose)

    def click_bug_project_select(self):
        self.click(self.bug_project_select)

    def click_bug_project_choose(self):
        self.click(self.bug_project_choose)

    def double_click_bug_version_select(self):
        self.double_click(self.bug_version_select)

    def click_bug_version_choose(self):
        self.click(self.bug_version_choose)

    def click_bug_datetime_select(self):
        self.click(self.bug_datetime_select)

    def click_bug_datetime_choose(self):
        self.click(self.bug_datetime_choose)

    def click_bug_system_select(self):
        self.click(self.bug_system_select)

    def click_bug_system_choose(self):
        self.click(self.bug_system_choose)

    def click_bug_browser_select(self):
        self.click(self.bug_browser_select)

    def click_bug_browser_choose(self):
        self.click(self.bug_browser_choose)

    def input_bug_title(self, content):
        self.input(self.bug_title_input, content)

    def click_bug_steps_frame(self):
        self.switch_to_frame(element=self.bug_steps_frame)

    def input_bug_steps(self, content):
        self.clear(self.bug_steps_input)
        self.input(self.bug_steps_input, content)

    def click_bug_save_button(self):
        self.click(self.bug_save_button)
