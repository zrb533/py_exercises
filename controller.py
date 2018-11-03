# -*- coding:utf-8 -*- #
import doctest
import HTMLTestRunner
from common.common import *
import unittest
import datetime
import os
from case.goods import *

try:
    suite = doctest.DocTestSuite()
    # goods
    suite.addTest(unittest.makeSuite(goods_select.TestGoodsSelect))
    # suite.addTest(unittest.makeSuite(goods_detail.TestGoodsDetail))

except (IOError,ModuleNotFoundError) as error:

    log_path = '..\\exception.log'
    logs(error, log_path)

# 生成测试结果
filename = 'c:\\exercises\\py_exercises\\result\\' + "py_exercises" + "_" + "result.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='py_exercises_report', description='py_exercises_report_description')
runner.run(suite)