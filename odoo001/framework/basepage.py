# -*- coding:utf8 -*-

#定位元素封装
import time
from framework.browser_engine import BrowserEngine
# from framework.browser_engine import TestSpase

class BasePage(object):

    # be = BrowserEngine()
    # driver = be.getdriver()
    def __init__(self, driver):
        self.driver = driver

    def find_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def find_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_class_name(self,class_name):
        return self.driver.find_element_by_class_name(class_name)

    def sleep(self, seconds):
        time.sleep(seconds)
