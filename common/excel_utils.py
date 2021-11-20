#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/11/20 
@File   : excel_utils.py  
=================================================="""
# 读取Excel工具类，底层封装，读取Excel文件后，返回[[], [], []]格式的数据
import os

import xlrd


class ExcelUtils:
    """
    先判断是否为Excel文件，然后再处理是xls、xlsx类型，并且文件存在
    """

    def __init__(self, excel_path, sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:     # 当sheet_name存在，通过sheet_name获取页签的数据
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)      # 当sheet_name不存在时，返回文件的第一个sheet
        return sheet

    @property
    def get_row_count(self):
        """
        获取Excel表行数
        :return:
        """
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        """
        获取Excel表列数
        :return:
        """
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self):
        """
        把Excel表的数据列表返回[[], [], []]
        :return:
        """
        all_excel_data = []
        for rownum in range(self.get_row_count):        # 假设self.get_row_count=5 取0，1,2,3,4
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum, colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xlsx')
    excel_data = ExcelUtils(excel_path).get_sheet_data_by_list()
    for l in excel_data:
        print(l)


