from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(BasePage):
    '''登陆页'''
    # 对象层
    url = '/user/login'
    user_name = (By.XPATH, '//input[@name="user_name"]')
    user_password = (By.XPATH, '//input[@name="user_password"]')
    submit_button = (By.XPATH, '//button[@type="submit"]')

    # 操作层
    # 登陆用户名
    def login_username(self, user_name):
        self.type_value(user_name, self.user_name)

    # 登陆密码
    def login_password(self, user_password):
        self.type_value(user_password, self.user_password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.submit_button).click()

    # 定义统一登陆接口
    def login_operator(self, user_name, user_password):
        self.login_username(user_name)
        self.login_password(user_password)
        self.login_button()

    # 校验元素
    # 密码为空时候的元素
    user_error_hint_loc = (By.XPATH, '//label[@for="user_name"]')
    password_error_hint_loc = (By.XPATH, '//label[@for="user_password"]')
    login_fail_loc = (By.XPATH, '//div[@class="message_one"]/div[@class="alert alert-error"]')

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def password_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text

    # 登陆错误提示
    def login_error_hint(self):
        return self.find_element(*self.login_fail_loc).text


if __name__ == "__main__":
    driver = TestChromeDriver().driver
    obj = LoginPage(driver)
    obj.login_operator('', '')
    print(obj.user_error_hint())
    print(obj.password_error_hint())
    sleep(10)
    # obj.quit()
