# -*- coding:utf8 -*-

#用例封装
# import unittest
# import sys,os,traceback
# from selenium.webdriver.common.keys import Keys
# from framework.browser_engine import BrowserEngine
#
# class test_readget(unittest.TestCase):
#
#     def setUp(self):
#         browser = BrowserEngine()
#         self.driver = browser.getdriver()
#         self.driver.implicitly_wait(2)
#
#     def test_quit_application(self):
#         # 离职申请
#         browser = BrowserEngine()
#         browser.open_browser(0, 4, 0)
#         sreach_window = self.driver.current_window_handle
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[1]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
#         lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
#         len(lists)
#         self.driver.find_element_by_class_name("o_list_button_add").click()
#         dl = self.driver.find_element_by_xpath("//*[@name='departuredate']/input")
#         dl.send_keys("2020/07/18")
#         dl.send_keys(Keys.ENTER)
#         self.driver.find_element_by_xpath("//*[@name='reason']").send_keys("+++...+++***")
#         self.driver.find_element_by_class_name("o_form_button_save").click()
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[1]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[2]").click()
#         self.driver.find_element_by_xpath("//*[@name='completed']").send_keys("++==++")
#         self.driver.find_element_by_xpath("//*[@name='unfinished']").send_keys("++==++")
#         self.driver.find_element_by_xpath("//*[@name='plan']").send_keys("++==++")
#         self.driver.find_element_by_xpath("//*[@name='handoverperson']").send_keys("++==++")
#         # handtime = self.driver.find_element_by_xpath("//*[@name='handoverdate']")
#         # handtime.click()
#         # handtime.send_keys("2020/07/15")
#         # handtime.send_keys(Keys.ENTER)
#         self.driver.find_element_by_class_name("o_form_button_save").click()
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[1]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
#         table = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
#         len(table)
#         # 断言
#         self.assertNotEqual(len(lists),len(table))
#
#     def tearDown(self):
#         test_method_name = self._testMethodName
#         runlog_path = r'F:\python_autotest\runlog'
#         os.chdir(runlog_path)
#         method_path = runlog_path + test_method_name
#         print(method_path)
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()