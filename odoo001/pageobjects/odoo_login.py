# -*- coding:utf8 -*-
#页面元素封装
from framework.basepage import BasePage

class Home_Login(BasePage):

    def __init__(self, driver):
        # super(Home_Baidu, self).__init__(driver)
        super(Home_Login,self).__init__(driver)
        self.driver = driver
