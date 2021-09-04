#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/30 23:48
=================================================="""

# 元素识别信息读取工具类 -- 方法二
import os
import time
from common.config_utils import local_config
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xlsx')


class ElementDataUtils:

    def __init__(self, module_name, excel_path=excel_path):
        """
        初始化Excel文件
        :param page_name:
        :param excel_path:
        """
        self.excel_path = excel_path
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.row_count = self.sheet.nrows

    def get_element_info(self, page_name):
        """
        组装数据字典信息
        :return:
        """
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == page_name:
                element_info = {
                    'element_name': self.sheet.cell_value(i, 1),
                    'locator_type': self.sheet.cell_value(i, 3),
                    'locator_value': self.sheet.cell_value(i, 4)
                }
                # 方法1：
                # timeout_value = self.sheet.cell_value(i ,5)
                # if element_info['timeout'] == '':
                #     timeout_value = 5.0
                # else:
                #     element_info['timeout'] = timeout_value
                # 方法2：通过类型来判定
                time_value = self.sheet.cell_value(i, 5)
                element_info['timeout'] = time_value if isinstance(time_value, float) else local_config.time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


if __name__ == '__main__':
    element = ElementDataUtils('login').get_element_info('login_page')
    print(element)
