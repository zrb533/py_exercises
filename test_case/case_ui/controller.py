# -*- coding:utf-8 -*- #
import doctest
import HTMLTestRunner
from common.common import *
import unittest

try:
    suite = doctest.DocTestSuite()
    # goods
    suite.addTest(unittest.makeSuite(ui_login.TestUILogin))
    # suite.addTest(unittest.makeSuite(goods_detail.TestGoodsDetail))

except (IOError,ModuleNotFoundError) as error:

    log_path = '../exception.log'
    logs(error, log_path)

# 生成测试结果
filename = '/Users/zhanglinquan/PycharmProjects/py_exercises/test_result/' + "py_exercises" + "_" + "case_ui_result.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='py_exercises_report', description='py_exercises_report_description')
runner.run(suite)