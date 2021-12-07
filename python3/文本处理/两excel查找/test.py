# import difflib
# def get_equal_rate(str1, str2):
#     """
#     比较两个字符串的相似程度
#     Args:
#         str1:第一个字符串
#         str2:第二个字符串
#     Returns:
#         返回两个字符串的相似程度（0~1）
#     """
#     return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

# str_1 = "入口活套1#套套量[%]"
# str_2 = "入口活套塔2实时套量"
# print(get_equal_rate(str_1, str_2))

    
# for cf in range(20):
#     match = difflib.get_close_matches(l, filelist, cutoff = 1.0 - cf/20.0, n=20)
#     if len(match) > 0:
#         matchlist.append(match[0])
#         flag = 1
#         break


#coding=utf8
import xlrd
import xlwt
import difflib


book = xlrd.open_workbook('2130归档.xls')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)

# 只有变量名sheet
sheet2 = book.sheet_by_index(1)
print("表单2名：", sheet2.name)
print("表单2行数：", sheet2.nrows)

workbook = xlwt.Workbook()
sheet_new = workbook.add_sheet('sheet2')
sheet_new.write(0, 0, '系统变量名')
sheet_new.write(0, 1, '已采集变量名称')

if __name__ == "__main__":

    matchlist = []  #已有的变量
    for i in range(1, sheet1.nrows):
        tagname = sheet1.cell_value(i, 0)	#sheet1每行的变量名
        # tagname = tagname.upper()
        matchlist.append(tagname)
    print("matchlist数量：" + str(len(matchlist)))
    # 每个变量名tag_num
    for tag_num in range(1,sheet2.nrows):
        tag_num_name = sheet2.cell_value(tag_num, 0)
        # tag_num_name = tag_num_name.upper()	#要匹配的变量名
        sheet_new.write(tag_num, 0, tag_num_name)	# 遍历sheet1
        print("要匹配的变量：" + tag_num_name)


        # for line in difflib.get_close_matches(tag_num_name, matchlist):
        #     print("匹配到："+line)
        # match = difflib.get_close_matches(tag_num_name, matchlist, n = 1, cutoff = 0.6)
        match = difflib.get_close_matches(tag_num_name, matchlist)
        if len(match) > 0:
            print("已匹配")
            for m in range(len(match)):
                sheet_new.write(tag_num, m+1, match[m])
            # matchlist.append(match[0])


    workbook.save('酸轧归档数据(2130采集).xls')
