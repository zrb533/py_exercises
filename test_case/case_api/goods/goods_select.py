# -*- coding:utf-8 -*- #
"""
auth: Colin
desc: goods select list
date: 20181102
"""
import requests
import json
import unittest
from common.common import *

class TestGoodsSelect(unittest.TestCase):


    def setUp(self):
        self.verificationErrors = []
        self.excel_path = '/Users/zhanglinquan/PycharmProjects/py_exercises/data/excel_api/goods/data_goods.xlsx'
        self.pe = parseExcel(self.excel_path)
        self.sheet = self.pe.set_sheet_by_name('goods_select')
        self.excel_url = self.sheet.cell(2,1).value
        self.excel_headers = self.sheet.cell(2,2).value
        self.excel_request_body = self.sheet.cell(2,3).value

    def test_goods_select(self):
        try:
            self.response = requests.post(self.excel_url, json=json.loads(self.excel_request_body),
                                          headers=json.loads(self.excel_headers))
            dict_json_response = self.response.json()
            response_code = dict_json_response['code']
            self.assertEqual(response_code, 1)
        except (IOError, TypeError) as error:
            log_path = "../goods_select_exception.log"
            logs(error, log_path)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestSuite
    suite.addTest(TestGoodsSelect("test_goods_select"))
    unittest.TextTestRunner.run(suite)