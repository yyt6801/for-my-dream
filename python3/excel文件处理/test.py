#coding=utf8
import xlrd
import xlwt

book = xlrd.open_workbook('123.xls')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)

workbook = xlwt.Workbook()
sheet_new = workbook.add_sheet('sheet2')
sheet_new.write(0, 0, '问题描述')
sheet_new.write(0, 1, '问题分类')

if __name__ == "__main__":
    for i in range(4056, 4248):
        row = sheet1.row(i)
        questions = sheet1.cell_value(i, 4)
        questions = questions.upper()
        print(sheet1.cell_value(i, 6))
        sheet_new.write(i - 4055, 0, questions)
        fenlei = ' '


        if "体检云" in questions:
            fenlei = '体检云系统问题'
            print("包含体检云,分类为 '体检云系统问题'")

        if "钼靶设备" in questions or "CT" in questions or "DR" in questions \
            or "PACS" in questions :
            fenlei = '医疗设备问题'
            print("分类为 '医疗设备问题'")

        if "删号" in questions:
            fenlei = '业务支持'
            print("包含删号,分类为 '业务支持'")

        if "停电" in questions:
            fenlei = '分院正常停电'
            print("包含停电,分类为 '分院正常停电'")

        if "电源" in questions or "关机" in questions \
        or "鼠标" in questions or "电脑" in questions \
        or "键盘" in questions or "驱动" in questions \
        or "USB" in questions or "接口" in questions \
        or "线" in questions or "屏幕" in questions \
        or "网卡" in questions or "主板" in questions \
        or "主机" in questions or "显示器" in questions \
        or "开机" in questions or "电池" in questions \
        or "插口" in questions or "叫号机" in questions \
        or "空间" in questions \
        or "死机" in questions or "硬盘" in questions :
            fenlei = 'IT硬件设备问题'
            print("分类为 'IT硬件设备问题'")

        if "PIS" in questions:
            fenlei = 'PIS系统问题'
            print("包含pis,分类为 'PIS系统问题'")

        if "MIS" in questions:
            fenlei = 'MIS系统问题'
            print("包含mis,分类为 'MIS系统问题'")

        if "LIS" in questions:
            fenlei = 'LIS系统问题'
            print("包含mis,分类为 'LIS系统问题'")

        if "打印" in questions:
            fenlei = '打印机问题'
            print("包含打印,分类为 '打印机问题'")
            
        sheet_new.write(i - 4055, 1, fenlei)
    workbook.save('jieguo1.xls')
