# 列出当前路径及其子目录下的所有文件
import os
filepath = 'E:\\files\\InformationSecurity\\formydream\\for-my-dream'


def show_dir(filepath):
    for d in os.listdir(filepath):
        path = os.path.join(filepath, d)
        if os.path.isdir(path):  #isdir()判断是否是目录
            show_dir(path)  #如果是目录，使用递归方法
        # print(path)
        if path.endswith(".html"):
            print('htmlx:' + path)


show_dir(filepath)
