#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/4 17:46
=================================================="""
import time
from selenium import webdriver
from common.browser import Browser
from common.base_page import BasePage


# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# time.sleep(2)
# driver.find_element_by_link_text('新闻').click()
# driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_link_text('地图').click()

driver = Browser().get_driver()
baae_page = BasePage(driver)
baae_page.open_url('https://www.baidu.com/')
baae_page.set_browser_max()
baae_page.implicitly_wait(10)
baae_page.wait(2)
baae_page.driver.find_element_by_link_text('新闻').click()
baae_page.driver.find_element_by_link_text('hao123').click()
baae_page.driver.find_element_by_link_text('地图').click()

baae_page.switch_to_window_by_title('百度一下，你就知道')
baae_page.driver.find_element_by_name('wd').send_keys('222')

baae_page.switch_to_window_by_title('百度新闻——海量中文资讯平台')
baae_page.driver.find_element_by_id('ww').send_keys('百度新闻')

baae_page.switch_to_window_by_title('百度地图')
baae_page.driver.find_element_by_id('sole-input').send_keys('长沙')

baae_page.switch_to_window_by_url('hao123.com')
baae_page.driver.find_element_by_name('word').send_keys('hao123')


