#coding=utf8
import xlrd
import xlwt
import numpy as np


book = xlrd.open_workbook('flatness233110305.xls')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)

workbook = xlwt.Workbook()
sheet_new = workbook.add_sheet('sheet2')
sheet_new.write(0, 0, '问题描述')
sheet_new.write(0, 1, '问题分类')

if __name__ == "__main__":
    for i in range(2, 311):
        row = sheet1.row(i)
        PRODUCTID = ''
        PRODUCTID = sheet1.cell_value(i, 0)
        PRODUCTID = PRODUCTID.upper()
        length = sheet1.cell_value(i, 1)
        print(length)
        
        asc_width_num = 34
        x=[]
        y=[]
        index = 0
        for fly_num in range(13, 47):
            x.append(index+1)
            y.append(sheet1.cell_value(i, fly_num+1))
            # x[index] = index+1
            # # print(sheet1.cell_value(i, fly_num+1))
            # y[fly_num] = sheet1.cell_value(i, fly_num+1)
            index =index+1
        print(x)
        print(y)
        # x = list(x)
        # y = list(y.values)
        # print(x)
        # print(y)
        # an = np.polyfit(list(x), list(y), 2)
        an = np.polyfit(x, y, 2)
        print(an)
        print(an[0])
        print(an[1])
        sheet_new.write(i, 0, PRODUCTID)
        sheet_new.write(i, 1, length)
        sheet_new.write(i, 2, float(an[0]))
        sheet_new.write(i, 3, float(an[1]))
    workbook.save('jieguo2.xls')