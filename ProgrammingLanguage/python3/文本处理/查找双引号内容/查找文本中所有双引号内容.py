# import re
# try:
#     file= open('results.txt', 'r',encoding='UTF-8')      # 打开文件
#     s = file.read()                   # 读取文件内容
#     lst = re.findall(r'"(.*?)(?<!\\)"', s)
#     for i in lst:
#         print(i)
# finally:
#     if file:
#         file.close()                     # 确保文件被关闭

import re
f = open('results.txt', 'r',encoding='UTF-8')
source = f.read()
f.close()
# r = r'Z.1.ZONE.*'
r = r'"(Z.1.ZONE.*?)(?<!\\)"'
s = re.findall(r,source)
for i in s:
    print(i)
# print(s)

# 查找字符串中双引号内容
# s = ''': 				if ( ((int)TAG("Z.1.ZONE2.CAL3_EJ2.POR1_OCCUPIED") == 1) && ((float)TAG("Z.1.ZONE2.CAL3_EJ2.POR1_ACT_SPEED") > 1 ) && ((const char*)(FormatString)TAG("Z.1.ZONE2.CAL3_EJ2.POR1_COIL_ID") != ""))//开卷机1开卷信号等于TRUE而且速度大于零'''
# lst = re.findall(r'"(.*?)(?<!\\)"', s)
# print(lst)




    ## 匹配所有以CRM.开头，以 空格 或 双引号 或 ] 结尾的内容
    # lst = re.findall(r'CRM.*?(?=[ ]|"|]|$)', s)