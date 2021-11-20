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
from common.log_utils import logger


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
        logger.info('点击测试模块按钮')

    def click_bug(self):
        self.click(self.bug_click)
        logger.info('点击bug模块按钮')

    def click_create_bug(self):
        self.click(self.create_bug_button)
        logger.info('点击创建bug按钮')

    def click_bug_module_select(self):
        self.click(self.bug_module_select)
        logger.info('点击bug所属模块下拉框')

    def click_bug_module_choose(self):
        self.click(self.bug_module_choose)
        logger.info('选择bug所属模块')

    def click_bug_project_select(self):
        self.click(self.bug_project_select)
        logger.info('点击bug所属项目下拉框')

    def click_bug_project_choose(self):
        self.click(self.bug_project_choose)
        logger.info('选择Bug所属项目')

    def double_click_bug_version_select(self):
        self.double_click(self.bug_version_select)
        logger.info('点击bug影响版本下拉框')

    def click_bug_version_choose(self):
        self.click(self.bug_version_choose)
        logger.info('选择bug影响版本')

    def click_bug_datetime_select(self):
        self.click(self.bug_datetime_select)
        logger.info('点击截止日期选择框')

    def click_bug_datetime_choose(self):
        self.click(self.bug_datetime_choose)
        logger.info('选择bug截止日志')

    def click_bug_system_select(self):
        self.click(self.bug_system_select)
        logger.info('点击bug影响操作系统下拉框')

    def click_bug_system_choose(self):
        self.click(self.bug_system_choose)
        logger.info('选择Bug影响操作系统')

    def click_bug_browser_select(self):
        self.click(self.bug_browser_select)
        logger.info('点击浏览器下拉框')

    def click_bug_browser_choose(self):
        self.click(self.bug_browser_choose)
        logger.info('选择浏览器版本')

    def input_bug_title(self, content):
        self.input(self.bug_title_input, content)
        logger.info('输入Bug标题 [%s]' % content)

    def click_bug_steps_frame(self):
        self.switch_to_frame(element=self.bug_steps_frame)
        logger.info('切换到bug描述输入框')

    def input_bug_steps(self, content):
        self.clear(self.bug_steps_input)
        logger.info('清除bug步骤输入框内容')
        self.input(self.bug_steps_input, content)
        logger.info('输入bug实现步骤')

    def click_bug_save_button(self):
        self.click(self.bug_save_button)



