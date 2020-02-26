import unittest
from Pages import *
import time
from logging import getLogger

logger = getLogger(__name__)


class TestLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = TestChromeDriver().driver

    def tearDown(self):
        self.driver.quit()

    def user_login_verify(self, user_name='', password=''):
        LoginPage(self.driver).login_operator(user_name, password)

    def test_login1(self):
        # 正常登陆
        self.user_login_verify()
        po = LoginPage(self.driver)
        self.assertEqual(po.user_error_hint(), '请输入会员登录名称！')
        self.assertEqual(po.password_error_hint(), '请输入密码！')
        po.screen_shot("user_pawd_empty")

    def test_login2(self):
        # 密码为空
        self.user_login_verify(user_name='linhao')
        po = LoginPage(self.driver)
        self.assertEqual(po.password_error_hint(), '请输入密码！')
        po.screen_shot("pawd_empty")

    def test_login3(self):
        # 用户名为空
        self.user_login_verify(password='test123')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_error_hint(), '请输入会员登录名称！')
        po.screen_shot("user_empty")

    def test_login4(self):
        # 用户名密码正确
        self.user_login_verify(user_name='linhao', password='test123')
        po = LoginPage(self.driver)
        self.assertEqual(self.driver.current_url, po.base_url + '/')
        po.screen_shot("login_success")

    def test_login5(self):
        # 用户名密码错误
        self.user_login_verify(user_name='lin', password='test')
        po = LoginPage(self.driver)
        self.assertIn("登录失败", po.login_error_hint())
        po.screen_shot("login_fail")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(TestLoginCase("test_login1"))
    suite.addTests(TestLoginCase("test_login2"))
    suite.addTests(TestLoginCase("test_login3"))
    suite.addTests(TestLoginCase("test_login4"))
    suite.addTests(TestLoginCase("test_login5"))
    runner = unittest.TextTestRunner()
    runner.run()
