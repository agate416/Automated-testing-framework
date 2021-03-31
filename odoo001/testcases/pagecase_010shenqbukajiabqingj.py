# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,traceback,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    #  申请
    def test_Leave_application(self):
        # 请假申请
        browser = BrowserEngine()
        browser.open_browser(0, 4, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[2]/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("//*【@class='o_cp_buttons']/div/button[1]").click()
        starttime = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[3]/tbody/tr/td[2]div/div/div[1]/input")
        starttime.send_keys("2020年08月25日 09时10分00秒")
        starttime.send_keys(Keys.ENTER)
        endtime = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[3]/tbody/tr/td[2]/div/div/div[2]/input")
        endtime.send_keys("2020年08月25日 18时10分00秒")
        endtime.send_keys(Keys.ENTER)
        contacts = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[4]/tbody/tr/td[2]/div/div/div[1]/input")
        contacts.send_keys("yueyue")
        relationship = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[4]/tbody/tr/td[2]/div/div/div[2]/input")
        relationship.send_keys("姐妹")
        contactstel = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[4]/tbody/tr/td[2]/div/div/div[3]/input")
        contactstel.send_keys("15136251415")
        self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[5]/tbody/tr/td[2]select").click()
        types = Select(self.driver.find_element_by_id("o_field_input_65"))
        types.select_by_index(1)
        self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[2]/table[6]/tbody/tr[2]/td[2]select").click()
        approved = Select(self.driver.find_element_by_id("o_field_input_67"))
        approved.select_by_index(1)
        self.driver.find_element_by_class_name("o_form_button_save").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        self.assertNotEqual(len(lie),len(lists))

    def test_Overtime_application(self):
        # 加班申请
        browser = BrowserEngine()
        browser.open_browser(0, 4, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[2]/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("//*【@class='o_cp_buttons']/div/button[1]").click()
        self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[4]/tbody/tr[2]/td[2]select").click()
        approved = Select(self.driver.find_element_by_id("o_field_input_84"))
        approved.select_by_index(1)
        starttime = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[5]/tbody/tr[2]/td[2]/div/div[1]/div/input")
        starttime.send_keys("2020年08月26日 19时10分00秒")
        starttime.send_keys(Keys.ENTER)
        endtime = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[5]/tbody/tr/td[2]/div/div[3]/div/input")
        endtime.send_keys("2020年08月26日 21时40分00秒")
        endtime.send_keys(Keys.ENTER)
        self.driver.find_element_by_class_name("o_form_button_save").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        self.assertNotEqual(len(lie), len(lists))

    def test_Replacement_application(self):
        # 补卡申请
        browser = BrowserEngine()
        browser.open_browser(0, 4, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[2]/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("//*【@class='o_cp_buttons']/div/button[1]").click()
        times = self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[4]/tbody/tr[1]/td[2]/div/input")
        times.send_keys("2020年08月24日 09时10分00秒")
        times.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[4]/tbody/tr[2]/td[2]select").click()
        replacement = Select(self.driver.find_element_by_id("o_field_input_8"))
        replacement.select_by_index(1)
        self.driver.find_element_by_xpath(
            "//*[@class='o_form_sheet']/div[1]/table[5]/tbody/tr[2]/td[2]select").click()
        approved = Select(self.driver.find_element_by_id("o_field_input_10"))
        approved.select_by_value("1532")
        self.driver.find_element_by_class_name("o_form_button_save").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        self.assertNotEqual(len(lie), len(lists))

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()