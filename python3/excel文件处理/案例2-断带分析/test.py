#coding=utf8
import xlrd
import xlwt

book = xlrd.open_workbook('123.xlsx')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)

workbook = xlwt.Workbook()
sheet_new = workbook.add_sheet('sheet2')
sheet_new.write(0, 0, '备注')
sheet_new.write(0, 1, '分类')
sheet_new.write(0, 2, '是否准确')
sheet_new.write(0, 3, '计划过渡厚度是否正常')
sheet_new.write(0, 4, '计划过渡厚度是否正常')
sheet_new.write(0, 5, '计划过渡厚度是否正常')
sheet_new.write(0, 6, '计划过渡厚度是否正常')
sheet_new.write(0, 7, '计划过渡厚度是否正常')
sheet_new.write(0, 8, '计划过渡厚度是否正常')
sheet_new.write(0, 9, '计划过渡厚度是否正常')
sheet_new.write(0, 10, '计划过渡厚度是否正常')
sheet_new.write(0, 11, '计划过渡厚度是否正常')
sheet_new.write(0, 12, '前行钢')
sheet_new.write(0, 13, '后行钢')

if __name__ == "__main__":
    for i in range(1, 355):
        row = sheet1.row(i)
        
        beizhu = sheet1.cell_value(i, 34) # 备注内容
        qianxinggangzhong = sheet1.cell_value(i, 39) # 前行钢钢种
        houxinggangzhong = sheet1.cell_value(i, 40) # 后行钢钢种
        guodu41 = sheet1.cell_value(i, 41) # 计划过渡厚度是否正常
        guodu42 = sheet1.cell_value(i, 42) # 计划过渡钢种是否正常
        guodu43 = sheet1.cell_value(i, 43) # 计划过渡厚度是否正常
        guodu44 = sheet1.cell_value(i, 44) # 计划过渡辊缝是否正常
        guodu45 = sheet1.cell_value(i, 45) # 计划过渡张力是否正常
        guodu46 = sheet1.cell_value(i, 46) # 计划过渡速度是否正常
        guodu47 = sheet1.cell_value(i, 47) # 计划过渡出口厚度是否正常
        guodu48 = sheet1.cell_value(i, 48) # 实际过渡厚度是否正常
        guodu49 = sheet1.cell_value(i, 49) # 实际过渡宽度是否正常
        biaomian = sheet1.cell_value(i, 58) # 表面数据
        QCDS = sheet1.cell_value(i, 59) # QCDS是否异常
        guodu_ZHAZHILI = sheet1.cell_value(i, 60) # 计划过渡轧制力是否正常



        
        beizhu = str(beizhu)

        fenlei = ' '
        shifouzhunque = 0
        

        if "焊缝" in beizhu:
            fenlei = '焊缝断带'
            if guodu41==0 and guodu42==0 and guodu43 ==0 and guodu43 ==0 and guodu44==0\
                or guodu45==0 and guodu46==0  and guodu47==0 and guodu48==0 and guodu49==0:
                shifouzhunque=1
            print("包含'焊缝',分类为 '焊缝断带'")

        if "高强" in beizhu:
            if qianxinggangzhong != houxinggangzhong and guodu42 ==1:
                fenlei = '高强断带'
                shifouzhunque=1
            print("包含'高强',分类为 '高强钢断带'")

        if "热轧" in beizhu  or "原料" in beizhu  or "板形" in beizhu  or "表面" in beizhu :
            fenlei = '原料质量'
            if biaomian ==1 or QCDS ==1:
                shifouzhunque=1
            print("包含'热轧',分类为 '原料质量'")

        if "材质过度" in beizhu or "材质转换" in beizhu or "轧制转换" in beizhu \
            or "材质过渡" in beizhu :
            fenlei = '过渡异常'
            if guodu41==1 or guodu42==1 or guodu43 ==1 or guodu43 ==1 or guodu44==1\
                or guodu45==1 or guodu46==1  or guodu47==1 or guodu48==1 or guodu49==1 or guodu_ZHAZHILI ==1:
                shifouzhunque=1
            print("包含'材质过度',分类为 '过渡异常'")

        if "冲孔" in beizhu:
            fenlei = '冲孔'
            if guodu41==0 and guodu42==0 and guodu43 ==0 and guodu43 ==0 and guodu44==0\
                or guodu45==0 and guodu46==0  and guodu47==0 and guodu48==0 and guodu49==0:
                shifouzhunque=1
            print("包含'冲孔',分类为 '冲孔'")
        # if "电源" in beizhu or "关机" in beizhu \
        # or "鼠标" in beizhu or "电脑" in beizhu \
        # or "键盘" in beizhu or "驱动" in beizhu \
        # or "USB" in beizhu or "接口" in beizhu \
        # or "线" in beizhu or "屏幕" in beizhu \
        # or "网卡" in beizhu or "主板" in beizhu \
        # or "主机" in beizhu or "显示器" in beizhu \
        # or "开机" in beizhu or "电池" in beizhu \
        # or "插口" in beizhu or "叫号机" in beizhu \
        # or "空间" in beizhu \
        # or "死机" in beizhu or "硬盘" in beizhu :
        #     fenlei = 'IT硬件设备问题'
        #     print("分类为 'IT硬件设备问题'")
       
        sheet_new.write(i, 0, beizhu)
        sheet_new.write(i, 1, fenlei)
        sheet_new.write(i, 2, shifouzhunque)
        sheet_new.write(i, 3, guodu41)
        sheet_new.write(i, 4, guodu42)
        sheet_new.write(i, 5, guodu43)
        sheet_new.write(i, 6, guodu44)
        sheet_new.write(i, 7, guodu45)
        sheet_new.write(i, 8, guodu46)
        sheet_new.write(i, 9, guodu47)
        sheet_new.write(i, 10, guodu48)
        sheet_new.write(i, 11, guodu49)
        sheet_new.write(i, 12, qianxinggangzhong)
        sheet_new.write(i, 13, houxinggangzhong)
    workbook.save('jieguo1.xls')
