# -*- coding:utf8 -*-

#  浏览器选择、启动及登录封装
import configparser
import time
from selenium import webdriver
from tools.read_excel import ReadExcel, ReadExcel2
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class  BrowserEngine(object):

    def getdriver(self):
        # 浏览器选择
        global driver,url,browser
        config = configparser.ConfigParser()
        file_path = 'F:\python_autotest\config.ini'
        config.read(file_path)
        browser = config.get('browserType', 'browserName')
        url = config.get('testServer', 'URL')
        if browser == 'Firefox':
            driver = webdriver.Firefox()
            return driver
        if browser == 'Ie':
            driver = webdriver.Ie()
            return driver
        if browser == 'Chrome':
            driver = webdriver.Chrome()
            return driver

    def open_browser(self,sheet, row, col):
        # 启动浏览器打开网页
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(1)
        # 用户登录
        driver.find_element_by_xpath('//*[@id="login"]').send_keys(ReadExcel().getValue(sheet, row, col))
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(ReadExcel().getValue(sheet, row, col+1))
        driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button').click()
        time.sleep(1)

    def New_Employee(self, sheet, row, col):
        # 页面数据填写
        driver.implicitly_wait(2)
        driver.find_element_by_name('name').send_keys(ReadExcel2().getValue2(sheet, row, col))
        driver.find_element_by_name('ldentityCard').send_keys(ReadExcel2().getValue2(sheet, row, col + 1))
        driver.find_element_by_name('Age').send_keys(ReadExcel2().getValue2(sheet, row, col + 3))
        driver.find_element_by_name('ContactWay').send_keys(ReadExcel2().getValue2(sheet, row, col + 4))
        driver.find_element_by_name('EmergencyContact').send_keys(ReadExcel2().getValue2(sheet, row, col + 14))
        driver.find_element_by_name('Relation').send_keys(ReadExcel2().getValue2(sheet, row, col + 15))
        driver.find_element_by_name('EmergencyContactTelephone').send_keys(ReadExcel2().getValue2(sheet, row, col + 16))
        driver.find_element_by_name('JobNumber').send_keys(ReadExcel2().getValue2(sheet, row, col + 18))
        driver.find_element_by_name('EmailAddress').send_keys(ReadExcel2().getValue2(sheet, row, col + 24))
        driver.find_element_by_name('Pay').send_keys(ReadExcel2().getValue2(sheet, row, col + 34))
        dropdown = driver.find_element_by_xpath('//*[@name="Station"]/div[1]/input')
        dropdown.click()
        dropdown.send_keys(ReadExcel2().getValue2(sheet, row, col + 19))
        dropdown.send_keys(Keys.ENTER)
        driver.find_element_by_id("ui-id-3")
        driver.find_element_by_link_text('C++工程师').click()
        cl = driver.find_element_by_xpath('//*[@name="Section"]/div[1]/input')
        cl.click()
        cl.send_keys(ReadExcel2().getValue2(sheet, row, col + 25))
        cl.send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@class="o_group hr_change"]/table[32]/tbody/tr/td[2]/select').click()
        mc = Select(driver.find_element_by_xpath("//*[@name='McTag']"))
        mc.select_by_index(1)
        dl = driver.find_element_by_xpath('//*[@name="attendance_type"]/div[1]/input')
        dl.click()
        dl.send_keys(ReadExcel2().getValue2(sheet, row, col + 38))
        dl.send_keys(Keys.ENTER)
