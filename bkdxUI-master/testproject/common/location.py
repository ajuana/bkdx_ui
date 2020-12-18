import unittest
import sys
from selenium import webdriver
# 定位封装
class Locations(object):
    def __init__(self):
        self.browser_type = None
    # 点击事件方法
    def Click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "classN":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()
    # 输入内容方法
    def Input(self, type, value, inputvalue):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "classN":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)












