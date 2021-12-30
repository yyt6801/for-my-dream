#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", mode='wt')
print("文件名: ", fo.name)

str = "test:www.runoob.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write(str)

# 读取文件所有内容
fo.seek(0, 0)
for index in range(6):
    line = next(fo)
    print("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()