# -*- coding:utf8 -*-

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

    def test_approval(self):
        # 转正审批
        browser = BrowserEngine()
        browser.open_browser(0, 4, 0)  # 对比数据
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()

        browser.open_browser(0, 9, 0)  # 直属上级、部门领导审批
        sreach_window = self.driver.current_window_handle
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[2]/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()  # 选择审批项
        self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()  # 点击编辑
        self.driver.find_element_by_xpath("//*[@class='o_view_manager_content']/div/div/div/div/div[2]/ul/li[2]").click()
        self.driver.find_element_by_xpath("//*[@name='those_remarks']").send_keys("++**")  # 填写简评
        self.driver.find_element_by_xpath("//*[@name='technical_evaluation']/div[2]/input").click()  # 选择技术评价
        self.driver.find_element_by_xpath("//*[@name='opinion']/div[3]/input").click()  # 选择审批意见
        self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[2]/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()  # 选择审批项
        self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()  # 点击编辑
        self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@name='department_comments']").send_keys("***+++***")  # 填写评语
        self.driver.find_element_by_xpath("//*[@name='department_opinion']/div[3]/input").click()  # 审批意见
        self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()

        browser.open_browser(0, 1, 0)  # 人事审批
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[2]/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()  # 选择审批项
        self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()  # 点击编辑
        self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[4]").click()
        self.driver.find_element_by_xpath("//*[@name='hr_comments']").send_keys("***+++***")  # 填写评语
        self.driver.find_element_by_xpath("//*[@name='hr_opinion']/div[3]/input").click()  # 审批意见
        field = self.driver.find_element_by_xpath("//*[@name='positive_date']/input")
        field.click()
        field.send_keys("2020/07/20")
        field.send_keys(Keys.ENTER)
        self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()

        browser.open_browser(0, 5, 0)  # 质量审批
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[2]/ul/li[4]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()  # 选择审批项
        self.driver.find_element_by_xpath('//*[@class="o_cp_buttons"]/div/div/button[1]').click()  # 点击编辑
        self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[2]/ul/li[5]").click()
        self.driver.find_element_by_xpath("//*[@name='qa_comments']").send_keys("***+++***")  # 填写评语
        self.driver.find_element_by_xpath("//*[@name='qa_opinion']/div[3]/input").click()  # 审批意见
        self.driver.find_element_by_class_name("o_form_button_save").click()  # 点击保存
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()

        browser.open_browser(0, 4, 0)  # 结果对比
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        table = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
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