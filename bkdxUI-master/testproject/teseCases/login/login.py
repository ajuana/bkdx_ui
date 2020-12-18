import unittest
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
sys.path.append('../../common')
from location import Locations
from webTool import WebTools
class TestLogin(unittest.TestCase):
    phone = "15218884975"
    password = "a1234567"
    # 执行一次
    @classmethod
    def setUpClass(self):
        self.Lat=Locations
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baokaodaxue.com/")
        self.driver.find_element_by_class_name('use_btn').click()
    def test_login(self):
        self.Lat.Click(self,"classN","login_btn")
        self.Lat.Input(self,"classN","phone",self.phone)
        self.Lat.Input(self, "classN", "pwd", self.password)
        self.Lat.Click(self, "classN", "submit_btn")
        print("登陆")
    def test_login2(self):
        print("sss")
    @classmethod
    def tearDownClass(self):  # 关闭浏览器
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()

















