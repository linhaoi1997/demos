import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from support.log import AutoTestLog

'''
注册-登录-查询-添加购物车-下单
'''
log = AutoTestLog()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BasePage(object):
    login_url = 'http://49.234.189.120'
    url = '/'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.open()
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        # print(self.driver.current_url)
        #查看页面是否和当前page类相同，如果不相同，切换到page类的url上
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if url in self.driver.current_url:
                break
            else:
                self.driver.switch_to.window(handle)
        # if url not in self.driver.current_url:
        #     self.driver.get(url)
        if self.driver.current_url == 'data:,':
            self.driver.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def type_value(self, key, loc):
        element = self.find_element(*loc)
        element.clear()
        element.send_keys(key)

    def screen_shot(self,name):
        if not name:
            now = time.strftime("%Y-%m-%d %H-%M-%S")
            screen_name = BASE_DIR + '/output/screenshot/' + now + '.png'
        else:
            screen_name = BASE_DIR + '/output/screenshot/' + name + '.png'
        log.get_log().debug('截图到' + screen_name)
        return self.driver.get_screenshot_as_file(screen_name)

    def quit(self):
        self.driver.quit()


class TestChromeDriver(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)


if __name__ == "__main__":
    driver = TestChromeDriver().driver
    obj = BasePage(driver)
    obj.screen_shot()
    time.sleep(10)
    obj.quit()
    pass