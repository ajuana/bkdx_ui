import unittest
import time
import sys
from BeautifulReport import BeautifulReport
sys.path.append('common')
from location import Locations
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('teseCases/login', pattern='login.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='报考大学UI测试报告1', report_dir='E:\workplace/bkdxweb/baokaodaxue/testproject/reports', theme='theme_default')




    # fp.close()












