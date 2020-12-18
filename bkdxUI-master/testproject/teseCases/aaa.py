# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from selenium import webdriver
from datetime import datetime, date, timedelta
import time
import unittest
import sys
class TestLogin(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baokaodaxue.com/")
        self.driver.find_element_by_class_name('use_btn').click()
    def test_case1(self):
        print("66")

    def tearDown(self):
        # self.driver.quit()
        print("sss")
if __name__ == '__main__':
    unittest.main()