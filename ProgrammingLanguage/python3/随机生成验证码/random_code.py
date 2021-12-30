# import random
# list1 = []
# for i in range(65, 91):
#     list1.append(chr(i))  #通过for循环遍历asii追加到空列表中
# for j in range(97, 123):
#     list1.append(chr(j))
# for k in range(48, 58):
#     list1.append(chr(k))
# ma = random.sample(list1, 6)
# print(ma)  #获取到的为列表
# ma = ''.join(ma)  #将列表转化为字符串
# print(ma)

import random, string
str1 = "0123456789"
str2 = string.ascii_letters  # string.ascii_letters 包含所有字母（大写或小写）的字符串
str3 = str1 + str2
ma1 = random.sample(str3, 6)  #多个字符中选取特定数量的字符
ma1 = ''.join(ma1)  #使用join拼接转换为字符串
print(ma1)  #通过引入string模块和random模块使用现有的方法
