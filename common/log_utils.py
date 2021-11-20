#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/22 9:35
日志模块，在控制台输出日志并写入文件
=================================================="""
import os
import logging
import time
from common.config_utils import local_config


current_path= os.path.dirname(__file__)
log_path=os.path.join(current_path, '..', local_config.log_path)


class LogUtils:

    def __init__(self, logger=None):
        self.log_name = os.path.join(log_path, 'UIText_%s.log' % time.strftime('%Y_%m_%d'))     # 一天的日志放一个文件中
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(local_config.log_level)

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')     # 追加模式  写日志文件
        self.fh.setLevel(local_config.log_level)
        self.ch = logging.StreamHandler()   # 控制台日志输出
        self.ch.setLevel(local_config.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
        )
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger


# 添加一个 logger 对象
# logger=LogUtils().logger
logger = LogUtils().get_log()


if __name__ == '__main__':
    logger.info('newdream')
    logger.warning('warning警告错误')
    logger.error('error错误日志')
    logger.critical('critical错误日志')

