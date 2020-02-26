import unittest
from support.HTMLTestRunner import HTMLTestRunner
import time

# 用例执行地址
dir = r'./testCases'

discover = unittest.defaultTestLoader.discover(dir, '*Case.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    reportName = r'E:\software\JetBrains\pycharm\projects\appium_test_project_wangyixinwen\output\report/' + now + 'report.html'
    with open(reportName, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='taobaoAutoTestReport', description=now + 'case')
        runner.run(discover)
