#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/30 23:34
=================================================="""
import os
import xlrd


current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('login_page')
row_count = sheet.nrows

element_infos = {}
for i in range(1, row_count):
    element_info = {
        'element_name': sheet.cell_value(i, 1),
        'locator_type': sheet.cell_value(i, 2),
        'locator_value': sheet.cell_value(i, 3),
        'timeout': sheet.cell_value(i, 4)
    }

    element_infos[sheet.cell_value(i, 0)] = element_info

print(element_infos)

