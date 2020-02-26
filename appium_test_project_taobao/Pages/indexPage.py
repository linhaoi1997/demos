from Pages.basePage import basePageClass
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

import time

class indexPageClass(basePageClass):
    '''淘宝首页'''
    # 对象层
    search_loc = (MobileBy.XPATH, '//*[contains(@content-desc,"搜索")]')  # 淘宝首页输入框
    searchKeys_loc = (MobileBy.ID, 'com.taobao.taobao:id/searchEdit')  # 输入框输入值
    searchBtn_loc = (MobileBy.ACCESSIBILITY_ID, '搜索')  # 点击输入框

    # 操作层

    def search(self):
        # print(len(self.driver.find_elements(*self.search_loc)))
        time.sleep(10)
        self.driver.find_element(*self.search_loc).click()

    def search_keys(self, key):
        self.driver.find_element(*self.searchKeys_loc).send_keys(key)

    def search_btn(self):
        self.driver.find_element(*self.searchBtn_loc).click()

    # 业务层

    def search_operator(self, key):
        self.search()
        self.search_keys(key)
        self.search_btn()


if __name__ == '__main__':
    obj = indexPageClass()
    obj.screenshot()
    # obj.wait()
    # obj.search_operator("suibian")
    # obj.exit()
    pass
