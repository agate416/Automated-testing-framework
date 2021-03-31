# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,traceback,time
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    def test_evaluate(self):
        # 试用期评价
        browser = BrowserEngine()
        browser.open_browser(0, 1, 0)  # 对比数据
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
        browser.open_browser(0, 9, 0)  # 部门评价
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div/button[1]").click()
        self.driver.find_element_by_xpath("//*[@name='first_evaluate']").send_keys("456++**--")  # 入职评价
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[2]").click()
        self.driver.find_element_by_xpath("//*[@name='second_evaluate']").send_keys("**++--**")  # 第二次月度评价
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@name='third_evaluate']").send_keys("**++--**")  # 第三次月度评价
        self.driver.find_element_by_class_name('o_form_button_save').click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
        browser.open_browser(0, 5, 0)  # 质量评价
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div/button[1]").click()
        self.driver.find_element_by_xpath("//*[@name='fqa_evaluate']").send_keys("456++**--")  # 入职评价
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[2]").click()
        self.driver.find_element_by_xpath("//*[@name='sqa_evaluate']").send_keys("**++--**")  # 第二次月度评价
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@name='tqa_evaluate']").send_keys("**++--**")  # 第三次月度评价
        self.driver.find_element_by_class_name('o_form_button_save').click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
        browser.open_browser(0, 1, 0)  # 人事确认
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div/button[1]").click()
        self.driver.find_element_by_xpath("//*[@name='FirstInterview']/input").click()
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[2]").click()
        self.driver.find_element_by_xpath("//*[@name='SecondInterview']/input").click()
        self.driver.find_element_by_xpath("//*[@class='o_notebook']/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@name='ThirdInterview']/input").click()
        self.driver.find_element_by_xpath("//*[@name='end_probation']/input").click()
        self.driver.find_element_by_class_name('o_form_button_save').click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[3]/li/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        table = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(table)
        # 断言
        self.assertNotEqual(len(lists), len(table))

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()