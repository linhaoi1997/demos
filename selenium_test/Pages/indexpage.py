from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class IndexPage(BasePage):
    '''首页'''
    # 对象层
    url = '/'
    search_loc = (By.XPATH, '//input[@class="search-text"]')

    # 操作层

    def search_operator(self, key):
        search_element = self.driver.find_element(*self.search_loc)
        search_element.send_keys(key)
        search_element.submit()


if __name__ == '__main__':
    driver = TestChromeDriver().driver
    obj = IndexPage(driver)
    obj.search_operator('test')
    sleep(10)
    obj.quit()
    pass
