from Pages.basepage import BasePage, TestChromeDriver
from selenium.webdriver.common.by import By
from time import sleep


class RegisterPage(BasePage):
    '''注册页'''
    # 对象层
    url = '/user/register'
    user_name = (By.XPATH, '//input[@name="user_name"]')
    user_password = (By.XPATH, '//input[@name="user_password"]')
    user_com_password = (By.XPATH, '//input[@name="user_com_passwd"]')
    user_email = (By.XPATH, '//input[@name="user_email"]')
    captcha_code = (By.XPATH, '//input[@name="captcha_code"]')
    agreement = (By.XPATH, '//input[@name="agreement"]')
    submit_button = (By.XPATH, '//button[@type="submit"]')

    # 操作层

    def register_operator(self, user_name, user_password, user_com_password, user_email,
                          captcha_code):
        self.type_value(user_name, self.user_name)
        self.type_value(user_password, self.user_password)
        self.type_value(user_com_password, self.user_com_password)
        self.type_value(user_email, self.user_email)
        self.type_value(captcha_code, self.captcha_code)
        self.find_element(*self.agreement).click()
        self.find_element(*self.submit_button).click()


if __name__ == "__main__":
    driver = TestChromeDriver().driver
    obj = RegisterPage(driver)
    obj.register_operator('linhao', 'test123', 'test123', '123456@163.com', '1234')
    sleep(10)
    # obj.quit()
