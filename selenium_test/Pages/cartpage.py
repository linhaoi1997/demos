from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(BasePage):
    '''商品页'''

    # 对象层
    url = '/cart'
    clear_cart = (By.XPATH, '//span[@class="shop-cart-coudan"]/a')
    to_settle_accounts = (By.XPATH, '//div[@class="shop-cart-action clearfix"]/a[1]')

    # 操作层
    def settle_accounts_operator(self):
        self.find_element(*self.to_settle_accounts).click()

    def clear_cart_operator(self):
        self.find_element(*self.clear_cart).click()


if __name__ == "__main__":
    driver = TestChromeDriver().driver
    from Pages.searchpage import SearchPage
    from Pages.goodspage import GoodsPage
    obj = SearchPage(driver)
    obj.click_goods()
    obj = GoodsPage(driver)
    obj.add_cart_submit_operator()
    obj = CartPage(driver)
    print(obj.driver.current_url)
    obj.settle_accounts_operator()
    sleep(10)
    # obj.quit()
