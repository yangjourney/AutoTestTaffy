# -*- coding: utf-8 -*-
import xlrd
import os
class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取标题
        self.row = self.table.row_values(0)
        #获取行数
        self.rowNum = self.table.nrows
        #获取列数
        self.colNum = self.table.ncols
        #当前列
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True
    #获取指定sheet的指定行列的单元格中的值
    def getCellValue(self, rowIndex, colIndex, xlsFilePath):
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[self]
        return table.cell(rowIndex, colIndex).value

    #获取行视图,根据Sheet序号获取该Sheet包含的所有行，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ],sheetIndex指示sheet的索引，0表示第一个sheet，依次类推,xlsFilePath是Excel文件的相对或者绝对路径
    def getAllRowsBySheetIndex(sheetIndex, xlsFilePath):
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[sheetIndex]
        rows = []
        rowNum = table.nrows # 总共行数
        rowList = table.row_values
        for i in range(rowNum):
            rows.append(rowList(i)) # 等价于rows.append(i, rowLists(i))
        return rows

    #获取某个Sheet的指定序号的行,sheetIndex从0开始,rowIndex从0开始
    def getRow(sheetIndex, rowIndex, xlsFilePath):
        rows = getAllRowsBySheetIndex(sheetIndex, xlsFilePath)
        return rows[rowIndex]

    #获取列视图,根据Sheet序号获取该Sheet包含的所有列，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ],sheetIndex指示sheet的索引，0表示第一个sheet，依次类推,xlsFilePath是Excel文件的相对或者绝对路径
    def getAllColsBySheetIndex(sheetIndex, xlsFilePath):
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[sheetIndex]
        cols = []
        colNum = table.ncols # 总共列数
        colList = table.col_values
        for i in range(colNum):
            cols.append(colList(i))
        return cols

    #获取某个Sheet的指定序号的列,sheetIndex从0开始,colIndex从0开始
    def getCol(sheetIndex, colIndex, xlsFilePath):
        cols = getAllColsBySheetIndex(sheetIndex, xlsFilePath)
        return cols[colIndex]
#if __name__=='__main__':
#    excel_path = os.path.abspath("E:/现代资源-屠宰单数据（称重定级导入模板）new.xlsx")
# 获取对应Excel文件中对应的Sheet，在测试编码过程中进行调整
#    excel = ExcelUtil(excel_path, 'Sheet1')
#    print(ExcelUtil.getCellValue(0, 4, 8, excel_path)) # 获取第一个sheet第四行第二列的单元格的值
