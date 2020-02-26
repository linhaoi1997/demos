from Pages.basePage import basePageClass
from appium.webdriver.common.mobileby import MobileBy
import  time


class myselfPageClass(basePageClass):

    login_register_loc=(MobileBy.ID,"com.netease.newsreader.activity:id/apt")#登陆注册元素
    mail_loc=(MobileBy.ID,'com.netease.newsreader.activity:id/a79')#使用邮箱登陆
    mailNumber_loc=(MobileBy.ID,'com.netease.newsreader.activity:id/ai3')#邮箱账户框元素
    mailPassword_loc=(MobileBy.ID,'com.netease.newsreader.activity:id/aj2')#邮箱密码框元素
    starUse_loc=(MobileBy.ID,'com.netease.newsreader.activity:id/aj4')#登陆元素

    concern_loc=(MobileBy.ID,'com.netease.newsreader.activity:id/bbo')#我的订阅元素

    def login_register(self):
        self.lowwait(self.login_register_loc).click()
        time.sleep(5)
        print(len(self.driver.find_elements(*self.mail_loc)))
        self.driver.find_elements(*self.mail_loc)[-1].click()

    def mail_login(self,keys):
        self.lowwait(self.mailNumber_loc).send_keys(keys)
        time.sleep(5)
        self.lowwait(self.mailNumber_loc).click()

    def mail_password(self,keys):
        self.lowwait(self.mailPassword_loc).send_keys(keys)
        self.lowwait(self.mailPassword_loc).click()

    def start_use(self):
        self.lowwait(self.starUse_loc).click()

    def concern(self):
        self.lowwait(self.concern_loc).click()


    #业务层
    def mail_Login_operator(self,mailNumber,mailPasswords):
        self.login_register()
        self.mail_login(mailNumber)
        self.mail_password(mailPasswords)
        self.start_use()

    def concern_operator(self):
        self.concern()

if __name__=="__main__":
    try:
        obj=myselfPageClass()
        # time.sleep(10)
        obj.table('我')
        print('-------')
        obj.mail_Login_operator('15774518534@163.com','shanbuzaigao123')

        obj.concern_operator()
        time.sleep(20)
    finally:
        obj.exit()

















