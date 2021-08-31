#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/29 22:12
=================================================="""
# 提取出所有页面公共的操作，做成页面类父类 BasePage
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger


# 启动浏览器后，把driver 传给BasePage
class BasePage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址：[%s]' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页的标题，标题为：[%s]' % value)
        return value

    # 元素的识别，通过分离处理的元素识别字典信息，返回一个元素
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'css_selector':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'class_name':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'partial_link_text':
            locator_type = By.PARTIAL_LINK_TEXT
        elif locator_type_name == 'link_text':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'tag_name':
            locator_type = By.TAG_NAME
        element = WebDriverWait(self.driver, locator_timeout).\
            until(lambda x: x.find_element(locator_type, locator_value_info))
        return element

    # 元素的操作
    # 封装元素输入操作
    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s] 输入框输入内容： %s' % (element_info['element_name'], content))

    # 元素点击操作
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s] 元素进行点击操作' % element_info['element_name'])
