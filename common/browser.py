#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/31 23:51
=================================================="""
# 浏览器类，用来提取driver
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import local_config
from common.log_utils import logger


current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '..', local_config.get_driver_path)


class Browser:

    def __init__(self, driver_path=driver_path):
        self.driver_path = driver_path
        self.driver_name = local_config.get_driver_name

    def get_driver(self):
        """

        :return:
        """
        if self.driver_name.lower() == 'chrome':
            return self.__get_chrome_driver()
        elif self.driver_name.lower() == 'firefox':
            return self.__get_firefox_driver()
        elif self.driver_name.lower() == 'edge':
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        """
        谷歌浏览器取消chrome受控制提示
        :return:
        """
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.driver_path, 'chromedriver.exe')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        logger.info('初始化chrome浏览器并启动')
        return driver

    def __get_firefox_driver(self):
        """
        封装firefox浏览器
        :return:
        """
        firefox_driver_path = os.path.join(self.driver_path, 'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        logger.info('初始化Firefox浏览器并启动')
        return driver

    def __get_edge_driver(self):
        """
        封装edge浏览器
        :return:
        """
        edge_driver_path = os.path.join(self.driver_path, 'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        logger.info('初始化edge浏览器并启动')
        return driver

