# 该文件把对数据库的操作封装起来，在其他需要操作该数据库的地方直接调用DB()即可
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# 操作数据库与操作文件类似，在读取修改开始和结束时都需要进行连接（打开），断开（关闭）等固定操作，文件读写时可以使用 with （上下文管理器）来简化操作，数据库当然也是可以的：

# #  以 pymysql 为例，实现通过 with 简化数据库操作

import pymysql


class DB():
    def __init__(self,
                 host='192.168.142.136',
                 port=3306,
                 db='test001',
                 user='root',
                 passwd='123456',
                 charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    db=db,
                                    user=user,
                                    passwd=passwd,
                                    charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()
