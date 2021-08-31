#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/1 16:30
=================================================="""
# 配置文件读取类

import os
import configparser


current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '../config/config.ini')


class ConfigUtils:

    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding='utf-8')

    @property
    def get_url(self):
        value = self.cfg.get('default', 'URL')
        return value

    @property
    def get_driver_path(self):
        value = self.cfg.get('default', 'driver_path')
        return value

    @property
    def get_driver_name(self):
        value = self.cfg.get('default', 'driver_name')
        return value

    @property
    def get_screenshot_path(self):
        value = self.cfg.get('default', 'screenshot_path')
        return value

    @property
    def time_out(self):
        value = float(self.cfg.get('default', 'time_out'))
        return value

    @property
    def screen_shot_path(self):
        value = self.cfg.get('default', 'screen_shot_path')
        return value

    @property
    def user_name(self):
        value = self.cfg.get('default', 'username')
        return value

    @property
    def pass_word(self):
        value = self.cfg.get('default', 'password')
        return value

    @property
    def log_path(self):
        value = self.cfg.get('default', 'log_path')
        return value

    @property
    def log_level(self):
        value = int(self.cfg.get('default', 'log_level'))
        return value

    @property
    def testdata_path(self):
        value = self.cfg.get('default', 'testdata_path')
        return value

    @property
    def case_path(self):
        value = self.cfg.get('default', 'case_path')
        return value

    @property
    def report_path(self):
        value = self.cfg.get('default', 'report_path')
        return value

    # 邮箱配置信息
    @property
    def smtp_server(self):
        value = self.cfg.get('email', 'smtp_server')
        return value

    @property
    def smtp_sender(self):
        value = self.cfg.get('email', 'smtp_sender')
        return value

    @property
    def smtp_senderpassword(self):
        value = self.cfg.get('email', 'smtp_senderpassword')
        return value

    @property
    def smtp_receiver(self):
        value = self.cfg.get('email', 'smtp_receiver')
        return value

    @property
    def smtp_cc(self):
        value = self.cfg.get('email', 'smtp_cc')
        return value

    @property
    def smtp_subject(self):
        value = self.cfg.get('email', 'smtp_subject')
        return value

    @property
    def smtp_body(self):
        value = self.cfg.get('email', 'smtp_body')
        return value

    @property
    def element_info_path(self):
        value = self.cfg.get('default', 'element_info_path')
        return value


# 封装一个读取配置文件的对象
local_config = ConfigUtils()


if __name__ == '__main__':
    print(local_config.get_url)
    print(local_config.get_driver_path)
    print(local_config.get_driver_name)
    print(local_config.time_out)
    print(local_config.screen_shot_path)
    print(local_config.log_level)
    print(local_config.log_path)
    print(local_config.smtp_cc)
    print(local_config.element_info_path)
