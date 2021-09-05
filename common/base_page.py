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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common.log_utils import logger
from common.config_utils import local_config


# 启动浏览器后，把driver 传给BasePage
class BasePage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 浏览器基础封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址：[%s]' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器窗口最小化')
        self.driver.implicitly_wait(10)

    def implicitly_wait(self, seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)
        logger.info('浏览器隐式等待 [%s] 秒' % seconds)

    def set_windows_size(self, height, width):
        self.driver.set_window_size(height, width)
        logger.info('浏览器窗口大小为[ %s * %s ]' % (height, width))

    def refresh(self):
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        logger.info('浏览器刷新操作')

    def get_url(self):
        value = self.driver.current_url
        logger.info('获取当前页面URL，地址为 [%s]' % value)
        return value

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页的标题，标题为：[%s]' % value)
        return value

    def get_page_source(self):
        value = self.driver.page_source
        logger.info('获取网页源代码, 代码为 [%s]' % value)
        return value

    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前tab页')

    def quite(self):
        self.driver.quit()
        logger.info('退出浏览器')

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
        logger.info('[%s] 元素识别成功' % element_info['element_name'])
        return element

    # 元素的操作
    # 封装元素输入操作
    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s] 输入框输入内容： [%s]' % (element_info['element_name'], content))

    # 元素点击操作
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s] 元素进行点击操作' % element_info['element_name'])

    def double_click(self, element_info):
        """
        元素双击操作
        :param element_info:
        :return:
        """
        self.wait(2)
        element = self.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()
        logger.info('[%s] 元素进行双击操作' % element_info['element_name'])

    # 获取文本信息
    def get_text(self, element_info):
        element = self.find_element(element_info)
        text = element.text
        logger.info('获取文本信息 [%s]' % text)
        # logger.error('元素识别失败，未能获取到元素信息，错误信息为：[%s]' % e.__str__())
        return text

    def clear(self, element_info):
        """
        清除文本框内容
        :param element_info:
        :return:
        """
        element = self.driver.find_element(element_info)
        self.wait(2)
        element.clear()
        logger.info('[%s] 元素进行清除操作' % element_info['element_name'])

    # 鼠标键盘封装 -- 鼠标移动到一个元素上
    def move_to_element_by_mouse(self, element_info):
        el = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(el).perform()
        self.wait(2)
        logger.info('鼠标移动到 [%s] 元素上' % element_info)

    # 鼠标长按不松的封装
    def long_press_element(self, element_info, seconds):
        el = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(el).pause(seconds).perform()
        logger.info('鼠标长按 [%s] 元素 [%s] 秒' % (element_info, seconds))

    # 鼠标右击操作封装
    def right_click_element(self, element_info):
        el = self.find_element(element_info)
        ActionChains(self.driver).context_click(el).perform()
        self.wait(2)
        logger.info('鼠标右击 [%s] 元素' % element_info)

    # 键盘的封装
    def ctrl_v(self):
        ActionChains(self.driver).key_down(Keys.CONTROL)\
            .send_keys('v').key_up(Keys.CONTROL).perform()
        logger.info('键盘按下 CTRL + V')

    # 固定等待
    def wait(self, seconds=local_config.time_out):
        time.sleep(seconds)
        logger.info('固定等待 [%s] 秒' % seconds)

    # 切框架
    # 思路1：通过元素element_info来定位
    # def switch_to_frame(self, element_info):
    #     element = self.find_element(element_info)
    #     self.driver.switch_to.frame(element)
    #     logger.info('浏览器切换框架')

    # 思路2：通过id或者name定位
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)
        logger.info('浏览器切换框架')

    # 思路3：
    def switch_to_frame(self, **element_dict):   # id=frame_id   name=frame_name   element=element_info
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)
        logger.info('浏览器切换框架')

    # 切句柄
    # 获取当前窗口句柄的封装
    def get_window_handle(self):
        nowhandle = self.driver.current_window_handle   # 获取当前窗口句柄
        logger.info('获取浏览器窗口，当前窗口为 [%s]' % nowhandle)
        return nowhandle

    def switch_to_windows_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)
        logger.info('切换浏览器窗口，当前窗口为 [%s]' % window_handle)

    # 更高级的封装--切换浏览器窗口-根据title
    def switch_to_window_by_title(self, title):
        all_handles = self.driver.window_handles
        for window_handle in all_handles:
            self.driver.switch_to.window(window_handle)
            try:
                if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                    logger.info('根据页面 title [%s] 切换浏览器窗口，当前窗口为 [%s]' % (title, window_handle))
                    break
            except Exception as e:
                continue

    # 更高级的封装--切换浏览器窗口-根据url
    def switch_to_window_by_url(self, url):
        all_handles = self.driver.window_handles
        for window_handle in all_handles:
            self.driver.switch_to.window(window_handle)
            try:
                if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                    logger.info('根据页面 url [%s] 切换浏览器窗口，当前窗口为 [%s]' % (url, window_handle))
                    break
            except Exception as e:
                continue

    # 切提示框
    # 处理思路1：
    # def switch_to_alert(self, action='accept', time_out=local_config.time_out):
    #     self.wait(time_out)
    #     alert = self.driver.switch_to.alert    # 弹出框对象
    #     alert_text = alert.text
    #     if action == 'accept':
    #         alert.accept()
    #         logger.info('提示框点击确认，提示信息 [%s]' % alert_text)
    #     else:
    #         alert.dismiss()
    #         logger.info('提示框点击取消，提示信息 [%s]' % alert_text)
    #     return alert_text

    # 扩展2：使用EC来检查
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if action == 'accept':
            alert.accept()
            logger.info('提示框点击确认，提示信息 [%s]' % alert_text)
        else:
            alert.dismiss()
            logger.info('提示框点击取消，提示信息 [%s]' % alert_text)
        return alert_text

    # 提示框输入文字
    # def switch_to_alert_prompt(self, send_keys, action='accept', time_out=local_config.time_out):
    #     self.wait(time_out)
    #     alert = self.driver.switch_to.alert
    #     alert_text = alert.text
    #     self.driver.switch_to.alert.send_keys(send_keys)
    #     self.wait(time_out)
    #     if action == 'accept':
    #         alert.accept()
    #         logger.info('提示框点击确认，提示信息 [%s], 输入框内输入内容 [%s]' % (alert_text, send_keys))
    #     else:
    #         alert.dismiss()
    #         logger.info('提示框点击取消，提示信息 [%s]' % alert_text)
    #     return alert_text

    # 方法2;
    def switch_to_alert_prompt(self, send_keys, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert     # 弹出框对象
        alert_text = alert.text
        self.driver.switch_to.alert.send_keys(send_keys)
        self.wait(2)
        if action == 'accept':
            alert.accept()
            logger.info('提示框点击确认，提示信息 [%s], 输入框内输入内容 [%s]' % (alert_text, send_keys))
        else:
            alert.dismiss()
            logger.info('提示框点击取消，提示信息 [%s]，未输入内容' % alert_text)
        return alert_text

    # js执行的封装
    # 步骤1：移除元素的value属性的封装
    def delete_element_attribute(self, element_info, attribute_name):
        el = self.find_element(element_info)
        Js = 'arguments[0].removeAttribute("value");' % attribute_name  # 移除元素的value属性
        self.__execute_script(Js, el)
        logger.info('移除 [%s] 属性' % attribute_name)

    # 修改元素的属性
    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        el = self.find_element(element_info)
        Js = 'arguments[0].setAttribute("%s", "%s");' % (attribute_name, attribute_value)
        self.__execute_script(Js, el)
        logger.info('修改元素属性[ %s: %s ]' % (attribute_name, attribute_value))

    # 滚动条的封装
    def scroll(self, heigh):
        self.wait(2)
        js = "window.scrollBy(0," + str(heigh) + ")"
        self.__execute_script(js)
        logger.info('浏览器滚动 [%s] 单位' % heigh)

    # 封装执行js脚本   继续封装成私有方法
    def __execute_script(self, js_str, element=None):
        if element:
            self.driver.execute_script(js_str, element)
        else:
            self.driver.execute_script(js_str)

    # 截图的封装
    def screenshot_as_file(self, *screenshot_path):
        if len(screenshot_path) == 0:  # 没有传地址，存放默认路径下
            screenshot_path = local_config.screen_shot_path
        else:
            screenshot_path = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')   # 如果文件名一致，就覆盖老的文件名
        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, '..', screenshot_path, 'UItest%s.png' % now)
        self.driver.save_screenshot(filename)

