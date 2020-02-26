from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

from support.log import AutoTestLog
import yaml

'''
上下滑动
左右滑动
获取toast
截图等
'''
log = AutoTestLog()


# print("执行了log代码")
#
# print(log)


class basePageClass():
    def __init__(self):

        with open(r'E:\software\JetBrains\pycharm\projects\appium_test_project_wangyixinwen\Pages\caps\taobao_caps.yaml', 'r',
                  encoding='utf-8') as f:
            taobao_caps = yaml.load(f)
            # print(taobao_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', taobao_caps)

        time.sleep(10)
        self.wait()

        # try:
        #     self.driver.find_element_by_id('com.netease.newsreader.activity:id/bu1').click()
        #     self.up_down(0.1,0.5)
        # except:
        #     pass
        time.sleep(10)



    def try_catch_by_text(self, text):
        try:
            self.driver.find_element_by_xpath("//*[@text='%s']" % text.format()).click()
        except Exception as e:
            print(e)

    def exit(self):
        self.driver.quit()
        log.get_log().debug('关闭驱动')

    def wait(self):
        self.driver.implicitly_wait(20)
        log.get_log().debug('隐式等待20s')

    def up_down(self, startY, endY):
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * startY, size['width'] * 0.5, size['height'] * endY,
                          2000)
        log.get_log().debug('开始上下滑动')

    def left_right(self, startX, endX):
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * startX, size['height'] * 0.5, size['width'] * endX, size['height'] * 0.5,
                          2000)
        log.get_log().debug('开始左右滑动')

    def toast(self, toasttext):
        try:
            toast_loc = (MobileBy.XPATH, '//*[contains(@text,"%s")]' % (toasttext))
            t = WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located(toast_loc))
        except Exception as e:
            print(e)
            log.get_log().debug('没有获取到toast')
        log.get_log().debug('获取toast: ')
        log.get_log().debug(t)

    def screenshot(self):
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        filename = r'E:\software\JetBrains\pycharm\projects\appium_test_project_wangyixinwen\output\screenshot/' + now + '.png'
        self.driver.get_screenshot_as_file(filename)
        log.get_log().debug('获取截图 ' + filename)

    def lowwait(self, loc):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))

    # table页的切换
    def table(self, tablename):
        if tablename == "首页":
            indexPage_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("首页")')
            self.lowwait(indexPage_loc).click()
        elif tablename == "视频":
            videoPage_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("视频")')
            self.lowwait(videoPage_loc).click()
        elif tablename == "圈子":
            groupPage_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("圈子")')
            self.lowwait(groupPage_loc).click()
        elif tablename == "我":
            myselfPage_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我")')
            self.lowwait(myselfPage_loc).click()

if __name__=="__main__":
    obj=basePageClass()
    time.sleep(10)
    obj.table('我')
    obj.exit()
























    # ...
