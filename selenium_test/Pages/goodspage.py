from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class GoodsPage(BasePage):
    '''商品页'''

    # 对象层
    url = '/goods'
    # url = '/list/goods'
    add_cart_submit = (By.XPATH, '//button[@id="add_cart_submit"]')
    to_settle_accounts = (By.XPATH, '//div[@id="message_url"]/a[2]')
    continue_shopping = (By.XPATH, '//div[@id="message_url"]/a[1]')

    # 操作层
    def add_cart_submit_operator(self, is_continue_shopping=False):
        # sleep(10)
        element = self.find_element(*self.add_cart_submit)
        # print(element)
        element.submit()
        element.click()
        if not is_continue_shopping:
            sleep(5)
            self.find_element(*self.to_settle_accounts).click()
        else:
            sleep(5)
            self.find_element(*self.continue_shopping).click()


if __name__ == "__main__":
    from Pages.searchpage import SearchPage

    driver = TestChromeDriver().driver
    obj = SearchPage(driver)
    obj.click_goods()
    obj = GoodsPage(driver)
    obj.add_cart_submit_operator()
    sleep(10)
    # obj.quit()
