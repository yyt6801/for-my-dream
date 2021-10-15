#coding=utf8
import xlrd
import xlwt

book = xlrd.open_workbook('zhushi.xls')
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
sheet_new.write(0, 0, '变量名')
sheet_new.write(0, 1, '注释')

if __name__ == "__main__":

	# 每个变量名tag_num
	for tag_num in range(1,sheet2.nrows):
		tag_num_name = sheet2.cell_value(tag_num, 0)
		tag_num_name = tag_num_name.upper()	#要匹配的变量名
		sheet_new.write(tag_num, 0, tagname)	# 遍历sheet1
		for i in range(1, sheet1.nrows):
			aa = 0
			tagname = sheet1.cell_value(i, 0)	#sheet1每行的变量名
			tagname = tagname.upper()
			if tagname == tag_num_name:
				aa = 1
				zhushi = sheet1.cell_value(i, 1)
				sheet_new.write(tag_num, 1, zhushi)
				break
		if aa == 0:
			print("无法匹配"+tag_num_name)
	workbook.save('jieguo1.xls')
