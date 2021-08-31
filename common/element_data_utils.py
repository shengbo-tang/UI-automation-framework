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

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xlsx')


class ElementDataUtils:

    def __init__(self, page_name, excel_path=excel_path):
        """
        初始化Excel文件
        :param page_name:
        :param excel_path:
        """
        self.excel_path = excel_path
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_count = self.sheet.nrows

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
                'locator_value': self.sheet.cell_value(i, 3),
                'timeout': self.sheet.cell_value(i, 4)
            }
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


if __name__ == '__main__':
    element = ElementDataUtils('login_page').get_element_info()
    print(element)