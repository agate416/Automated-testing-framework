# -*- coding:utf-8 -*-

#用例封装
import unittest
import sys,os,traceback,time
from selenium.webdriver.common.keys import Keys
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    def test_probative(self):
        # 正常创建试用员工面谈记录
        browser = BrowserEngine()
        browser.open_browser(0, 1, 0)
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        # self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/a").click()
        self.driver.find_element_by_class_name("o_list_button_add").click()
        # self.driver.find_element_by_class_name("o_main_content")
        # self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/button[1]").click()
        name = self.driver.find_element_by_xpath("//*[@name='name']")
        name.click()
        name.send_keys('DUOLA')
        self.driver.find_element_by_xpath("//*[@name='JobNumber']").click()
        field = self.driver.find_element_by_xpath("//*[@name='ExpectedDateOfConversion']/input")
        field.click()
        field.send_keys("2020/07/20")
        field.send_keys(Keys.ENTER)
        interone = self.driver.find_element_by_xpath("//*[@name='first_interviewer']")
        interone.click()
        interone.send_keys("***")
        self.driver.find_element_by_xpath("//*[@name='FirstAnswer_one']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='FirstAnswer_two']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='FirstAnswer_three']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='FirstAnswer_four']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='FirstAnswer_five']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[2]").click()
        intertwo =self.driver.find_element_by_xpath("//*[@name='second_interviewer']")
        intertwo.click()
        intertwo.send_keys("***")
        self.driver.find_element_by_xpath("//*[@name='SecondAnswer_one']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='SecondAnswer_two']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='SecondAnswer_three']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='SecondAnswer_four']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='SecondAnswer_five']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[3]").click()
        interthree = self.driver.find_element_by_xpath("//*[@name='third_interviewer']")
        interthree.click()
        interthree.send_keys("***")
        self.driver.find_element_by_xpath("//*[@name='ThirdAnswer_one']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='ThirdAnswer_two']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='ThirdAnswer_three']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='ThirdAnswer_four']").send_keys("***+++")
        self.driver.find_element_by_xpath("//*[@name='ThirdAnswer_five']").send_keys("***+++")
        self.driver.find_element_by_class_name('o_form_button_save').click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        table = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(table)
        # 断言
        self.assertNotEqual(len(lists),len(table))

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()