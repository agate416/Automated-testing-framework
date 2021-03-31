# -*- coding:utf8 -*-

#用例封装
# import unittest
# import sys,os,traceback,time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from framework.browser_engine import BrowserEngine
#
# class test_readget(unittest.TestCase):
#
#     def setUp(self):
#         browser = BrowserEngine()
#         self.driver = browser.getdriver()
#         self.driver.implicitly_wait(2)
#
#     def test_quit_approval(self):
#         # 离职审批
#         browser = BrowserEngine()
#         browser.open_browser(0, 1, 0)
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[8]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
#         lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
#         len(lists)
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#         browser.open_browser(0, 9, 0)  # 部门审批
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[2]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[3]").click()
#         self.driver.find_element_by_xpath("//*[@name='officesupplies']/div[3]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='card']/div[3]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='document']/div[3]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='trainingmaterials']/div[3]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='todos']/div[3]/input").click()
#         # person = self.driver.find_element_by_xpath("//*[@name='handoverperson']")
#         # time.sleep(3)
#         # person.click()
#         # person.send_keys("***")
#         # handtime = self.driver.find_element_by_xpath("//*[@name='handoverdate']")
#         # handtime.click()
#         # handtime.send_keys("2020/07/15")
#         # handtime.send_keys(Keys.ENTER)
#         self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#
#         browser.open_browser(0, 2, 0)  # 行政审批
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[3]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[4]").click()
#         attendance = self.driver.find_element_by_xpath("//*[@name='attendance']")
#         attendance.clear()
#         attendance.send_keys("17")
#         self.driver.find_element_by_xpath("//*[@name='deduction']").send_keys(" ")
#         sl = Select(self.driver.find_element_by_xpath("//*[@name='other']"))
#         sl.select_by_index(1)
#         self.driver.find_element_by_xpath("//*[@name='reviewer']").send_keys("蒲")
#         self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#
#         browser.open_browser(0, 7, 0)  # IT审批
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[4]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[5]").click()
#         self.driver.find_element_by_xpath("//*[@name='computerpassworld']").send_keys("123456")
#         self.driver.find_element_by_xpath("//*[@name='cancellationaccount']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='takeback']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='itreviewer']").send_keys("刘")
#         self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#
#         browser.open_browser(0, 6, 0)  # 财务审批
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[5]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[6]").click()
#         self.driver.find_element_by_xpath("//*[@name='borrowing']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='reimbursement']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='adminreviewer']").send_keys("张")
#         self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#
#         browser.open_browser(0, 1, 0)  # HR审批
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[6]/a").click()
#         self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[7]").click()
#         self.driver.find_element_by_xpath("//*[@name='leaveapplication']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='cancelemail']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='signout']/div[2]/input").click()
#         self.driver.find_element_by_xpath("//*[@name='hrreviewer']").send_keys("刘")
#         self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()

#         # browser.open_browser(0, 8, 0)
#         # self.driver.find_element_by_link_text("劳动关系").click()
#         # self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[7]/a").click()
#         # self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
#         # self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
#         # self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()
#         # self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[8]").click()
#         # self.driver.find_element_by_xpath("//*[@name='generareviewer']").send_keys("刘")
#         # self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
#         # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
#         # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
#         # browser.open_browser(0, 1, 0)
#         self.driver.find_element_by_link_text("劳动关系").click()
#         self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[2]/li[8]/a").click()
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
# if __name__=='__main__':
#     unittest.main()