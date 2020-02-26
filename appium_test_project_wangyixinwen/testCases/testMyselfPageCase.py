import unittest
from Pages.myselfPage import myselfPageClass
import time
import pytest

# class TestMyselfCaseClass(unittest.TestCase):
#
#     def setUp(self):
#         self.obj = myselfPageClass()
#         self.obj.table('我')
#
#     def tearDown(self):
#         self.obj.exit()
#
#     def test_MailLogin(self):
#         # 正常登陆
#         try:
#             self.obj.mail_Login_operator('15774518534@163.com', 'shanbuzaigao123')
#             print('正常登陆')
#             # 断言
#         except Exception as e:
#             print(e)
#             self.obj.screenshot()
#
#     def test_Concern(self):
#         try:
#             self.obj.concern_operator()
#             print('打开我的关注')
#             # 断言
#         except Exception as e:
#             print(e)
#             self.obj.screenshot()

#用pytest来写
@pytest.mark.usefixtures('init_login')
class TestMyselfCaseClass():

    # def testlogin(self,init_login):
    #     try:
    #         print('正常登陆')
    #         # 断言
    #     except Exception as e:
    #         print(e)
    #         self.obj.screenshot()

    @pytest.mark.smoke
    def testConcern(self,init_login):
        try:
            init_login.concern_operator()
            print('打开我的关注')
            # 断言
        except Exception as e:
            print(e)
            self.obj.screenshot()

if __name__ == '__main__':
    pytest.main(["-s","testMyselfPageCase.py"])
