#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/30 23:48
=================================================="""
# 元素识别信息读取工具类
import os
import time
import xlrd
from common.config_utils import local_config
from common.log_utils import logger

current_path = os.path.dirname(__file__)
# excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xlsx')
excel_path = os.path.join(current_path, '..', local_config.element_info_path)


class ElementDataUtils:

    def __init__(self, module_name, page_name, excel_path=excel_path):
        """
        初始化Excel文件
        :param page_name:
        :param excel_path:
        """
        self.excel_path = os.path.join(excel_path, module_name, page_name + '.xlsx')
        self.workbook = xlrd.open_workbook(self.excel_path)
        logger.info('打开元素识别信息excel: [%s]' % self.excel_path)
        # self.sheet = self.workbook.sheet_by_name(module_name)
        self.sheet = self.workbook.sheet_by_index(0)    # 取第一个页签
        self.row_count = self.sheet.nrows
        self.page_name = page_name

    def get_element_info(self):
        """
        组装数据字典信息
        :return:
        """
        element_infos = {}
        for i in range(1, self.row_count):
            element_info = {
                'element_name': self.sheet.cell_value(i, 1),
                'locator_type': self.sheet.cell_value(i, 2),
                'locator_value': self.sheet.cell_value(i, 3)
            }
            # 方法1：
            # timeout_value = self.sheet.cell_value(i ,5)
            # if element_info['timeout'] == '':
            #     timeout_value = 5.0
            # else:
            #     element_info['timeout'] = timeout_value
            # 方法2：通过类型来判定
            time_value = self.sheet.cell_value(i, 4)
            element_info['timeout'] = time_value if isinstance(time_value, float) else local_config.time_out
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        logger.info('已成功从excel表中读取元素识别数据')
        return element_infos


if __name__ == '__main__':
    element = ElementDataUtils('bug', 'bug_page').get_element_info()
    for i in element.items():
        print(i)
