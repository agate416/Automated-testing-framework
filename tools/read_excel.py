# -*- coding:utf8 -*-

import xlrd

class ReadExcel():

    def __init__(self, excelPath="F:\YXexcel\denglu.xlsx"):
        self.excelPath = excelPath

    def readExcle(self, sheet, row, col):
        workEx = xlrd.open_workbook(self.excelPath)  # 打开excel表格
        sheetEx = workEx.sheet_by_index(sheet)  # 获得sheet对象
        cellValue = sheetEx.cell_value(row, col)  # 获取对象的值
        return cellValue

    def getValue(self, sheet, row, col):
        return self.readExcle(sheet, row, col)

class ReadExcel2():
    def __init__(self,excelPath="F:\YXexcel\denglu.xlsx"):
        self.excelPath = excelPath

    def readExcle(self, sheet, row, col):
        workEx = xlrd.open_workbook(self.excelPath)  # 打开excel表格
        sheetEx = workEx.sheet_by_index(sheet)  # 获得sheet对象
        cellValue = sheetEx.cell_value(row, col)  # 获取对象的值
        return cellValue

    def getValue2(self, sheet, row, col):
        return self.readExcle(sheet, row, col)