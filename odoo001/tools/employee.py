# -*- coding:utf8 -*-

import xlrd

class Read_em_Excel():

    def __init__(self,excelPath="F:\YXexcel\employee.xlsx"):
        self.excelPath = excelPath
    def read_em_Excle(self,sheet,row,col):
        workEx = xlrd.open_workbook(self.excelPath)
        sheetEx = workEx.sheet_by_index(sheet)
        cellValue = sheetEx.cell_value(row,col)
        return cellValue

    def get_em_Value(self,sheet,row,col):
        return self.read_em_Excle(sheet,row,col)