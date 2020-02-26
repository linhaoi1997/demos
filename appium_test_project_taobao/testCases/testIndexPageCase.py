from Pages.indexPage import indexPageClass
from appium import webdriver
from support.log import AutoTestLog
import ddt
import unittest

import time
log = AutoTestLog()
list = ["111", "suibian", "sony", "<script>alert(1)</script>"]


@ddt.ddt
class testIndexPageCaseClass(unittest.TestCase):

    def setUp(self):
        self.obj = indexPageClass()
        log.get_log().debug('测试开始')

    def tearDown(self):
        # self.obj.exit()
        log.get_log().debug('测试结束')

    @ddt.data(*list)
    def testcase1(self, data):
        try:
            self.obj.search_operator(data)
            # 断言
        except Exception as msg:
            print(msg)
            self.assertIsNotNone(msg)
            self.obj.screenshot()
        finally:
            self.obj.exit()


if __name__ == "__main__":
    unittest.main()
    pass
