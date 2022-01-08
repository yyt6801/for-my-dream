# -*- coding: utf-8 -*-

import configparser
import os
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")
print(cfgpath)  # cfg.ini的路径
# 创建管理对象
conf = configparser.ConfigParser()
 
# 读ini文件
conf.read(cfgpath, encoding="utf-8")  # python3
 
# 获取所有的section
sections = conf.sections()
print(sections)  # 返回list
 
items = conf.items('webservice')
print(items[0][1])  # list里面对象是元祖