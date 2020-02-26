import pytest
from Pages.myselfPage import myselfPageClass
from appium import webdriver

@pytest.fixture()
def init_login():
    #登陆函数，根据元素（登陆/注册）判断用户是否登陆
    obj=myselfPageClass()
    obj.table('我')
    targ=0
    try:
        obj.lowwait(obj.login_register_loc)
        targ=1
    except:
        pass

    if  targ==1:
        obj.mail_Login_operator('15774518534@163.com', 'shanbuzaigao123')

    yield obj

    obj.exit()