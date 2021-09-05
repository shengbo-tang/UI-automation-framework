#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/5 23:04
=================================================="""
import unittest
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config


class SeleniumBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.get_url

    def setUp(self) -> None:
        self.driver = Browser().get_driver()
        self.base_page = BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait(10)
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        self.base_page.wait(2)
        self.base_page.quite()

