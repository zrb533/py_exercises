# -*-coding:utf-8-*- #
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from common.common import *
import unittest

class TestUILogin(unittest.TestCase):


    def setUp(self):
        self.verificationErrors = []
        self.login_data_excel_path = "/Users/zhanglinquan/PycharmProjects/py_exercises/data/excel_ui/login/login.xlsx"
        self.pe = parseExcel(self.login_data_excel_path)
        self.sheet = self.pe.set_sheet_by_name("login")
        self.url = self.sheet.cell(2, 1).value
        self.email = self.sheet.cell(2, 2).value
        self.password = self.sheet.cell(2, 3).value
        self.verifycode = self.sheet.cell(2, 4).value

    def test_login(self):
        chrome_options = Options()
        self.browser = webdriver.Chrome\
            (chrome_options=chrome_options, executable_path=r'/usr/local/bin/chromedriver')
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_id("email").send_keys(self.email)
        self.browser.find_element_by_id("password").send_keys(self.password)
        self.browser.find_element_by_id("authcode").send_keys(self.verifycode)
        self.remember_me_checked = self.browser.find_element_by_class_name\
            ("ant-checkbox-input").get_property("checked")
        if self.remember_me_checked:
            self.browser.find_element_by_xpath\
                ('//*[@id="root"]/div/div[1]/div[2]/div/form/div[5]/div/div/span/button').click()
        else:
            self.remember_me_checked.click()
            self.browser.find_element_by_xpath\
                ('//*[@id="root"]/div/div[1]/div[2]/div/form/div[5]/div/div/span/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath\
            ('//*[@id="root"]/div/div/div[2]/div[1]/div/div/span/span[2]').click()
        self.user_name = self.browser.find_element_by_xpath\
            ('//*[@id="root"]/div/div/div[2]/div[1]/div/div/span/span[2]').text

        self.assertEqual(self.user_name, u"张林权")

    def tearDown(self):
        self.browser.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestSuite
    suite.addTest(TestUILogin("test_login"))
    unittest.TextTestRunner.run(suite)