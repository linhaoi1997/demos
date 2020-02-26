from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class SearchPage(BasePage):
    '''搜索页'''
    # 对象层
    url = '/list/goodsSearch'
    goods = (By.XPATH, '//div[@class="item-thumb"]/a')

    # 操作层
    def filter_goods(self, elements, title_information):
        elements = self.find_elements(*self.goods)
        want_elements = []
        for element in elements:
            if title_information in element.get_attribute('title'):
                want_elements.append(element)
        if len(want_elements) == 1:
            return want_elements[0]
        else:
            raise Exception('too many goods')

    def click_goods(self):
        goods = self.find_element(*self.goods)
        goods.click()


if __name__ == "__main__":
    driver = TestChromeDriver().driver
    obj = SearchPage(driver)
    obj.click_goods()
    sleep(10)
    # obj.quit()
