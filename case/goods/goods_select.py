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
        self.url = "http://jadmins.beta.orderplus.com/goods/select"
        self.header = {"Cookie": "SESSION=e62c7a8e-116d-4d79-914b-23fd5f213013", "Content-Type": "application/json"}
        self.request_body = {"pageSize": 10}

    def test_goods_select(self):
        try:
            self.response = requests.post(url=self.url, data=json.dumps(self.request_body), headers=self.header)
            dict_json_response = self.response.json()
            response_code = dict_json_response['code']
            self.assertEqual(response_code, 1)
        except (IOError, TypeError) as error:
            log_path = "..\\goods_select_exception.log"
            logs(error, log_path)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestSuite
    suite.addTest(TestGoodsSelect("test_goods_select"))
    unittest.TextTestRunner.run(suite)