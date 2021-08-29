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
log_path=os.path.join(current_path,'../logs/UI_test.log')


class LogUtils:

    def __init__(self,log_path=log_path):
        self.logfile_path=log_path
        self.logger=logging.getLogger(__name__)  # 创建日志对象
        self.logger.setLevel(level=logging.INFO)
        file_log=logging.FileHandler(self.logfile_path, encoding='utf-8')   # 创建文件日志对象
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def get_logger(self):
        return self.logger


# 添加一个 logger 对象
# logger=LogUtils().logger
logger = LogUtils().get_logger()


if __name__ == '__main__':
    logger.info('newdream')
    logger.warning('warning警告错误')
    logger.error('error错误日志')
    logger.critical('critical错误日志')

