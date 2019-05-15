# -*- coding:utf-8 -*- 
import sys
import os
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import unittest
import time

cwd = os.getcwd()
sys.path.append(os.getcwd())
#print(cwd)

test_dir = './case'
testsuit = defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == "__main__":  
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './result/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='发布会签到系统接口自动化测试',
                            description='test')
    runner.run(testsuit)
    fp.close()