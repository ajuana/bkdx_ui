# 浏览器操作
import os
import sys
import time
import unittest

from selenium import webdriver
class WebTools(object):
    def __init__(self):
        self.browser_type = None
    # 跳转页面
    def webopen(self, page):
        self.driver = webdriver.Chrome()
        self.driver.get(page)

        # 打开浏览器的方法
    def Openbrowser(self):
        if self.browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            self.driver = webdriver.Ie()
        elif self.browser_type == '':
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)













