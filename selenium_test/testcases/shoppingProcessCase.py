import unittest
from Pages import *
import time
from logging import getLogger

logger = getLogger(__name__)


class TestShoppingProcessCase(unittest.TestCase):

    def setUp(self):
        self.driver = TestChromeDriver().driver

    def tearDown(self):
        self.driver.quit()

    def test_shopping_process(self):
        # 正常登陆
        try:
            user_name = 'linhao'
            user_password = 'test123'
            self.obj = LoginPage(self.driver)
            self.obj.login_operator(user_name, user_password)
            logger.debug('正常登陆')

            self.obj = IndexPage(self.driver)
            self.obj.search_operator('小米')
            logger.debug('首页搜索正常')

            self.obj = SearchPage(self.driver)
            self.obj.click_goods()
            logger.debug('搜索页点击商品正常')

            self.obj = GoodsPage(self.driver)
            self.obj.add_cart_submit_operator()
            logger.debug('添加购物车正常')

            self.obj = CartPage(self.driver)
            self.obj.settle_accounts_operator()
            logger.debug('进入结算页面正常')

            # 断言
        except Exception as e:
            logger.debug(e)
            self.obj.screenshot()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestShoppingProcessCase("test_shopping_process"))

    runner = unittest.TextTestRunner()
    runner.run()
