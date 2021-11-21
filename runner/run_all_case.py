#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/11/21 18:37
@File   : run_all_case.py
@Desc   ：执行层脚本，批量执行脚本
=================================================="""
import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import local_config


current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, '..', local_config.case_path)
report_path = os.path.join(current_path, '..', local_config.report_path)


class RunAllCase:

    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '禅道UI自动化测试报告'
        self.description = 'UI自动脚本初版_tangshengbo'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_case.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='Tangshengbo')
        runner.run(all_suite)
        fp.close()
        return dir_path


if __name__ == '__main__':
    dir_path = RunAllCase().run()
    print(dir_path)
