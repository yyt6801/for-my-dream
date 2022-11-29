# -*- coding:utf-8 -*-
import os
import ibm_db

# 数据库连接信息
# db_url = "DATABASE=moiac;SCHEMA=moiase;HOSTNAME=199.188.166.110;PORT=60000;PROTOCOL=TCPIP;UID=moiase;PWD=moiase;"
db_url = "Driver={IBM DB2 ODBC DRIVER};HostName=192.168.50.16;Protocol=TCPIP; Port=50000;Database=MGLZ;Scheme=QU;Uid=db2inst1;Pwd=p@ssw0rd"

# 要查询的表名
tab_name = "QU.TB_TEST"

# 结果文件
file_name = "%s.sql" % (tab_name)
# 删除已存在的文件
if os.path.exists(file_name):
    os.remove(file_name)

# 查询sql
select_sql = """select * from %s""" % (tab_name)

# 连接数据库执行sql获取数据
try:
    # 连接数据库
    conn = ibm_db.connect(db_url, "", "")
    # 关闭自动提交
    ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_OFF)
    # 执行SQL语句
    stmt = ibm_db.exec_immediate(conn, select_sql)
    res = ibm_db.fetch_assoc(stmt)
    # res=ibm_db.fetch_both(stmt)
    # res = ibm_db.fetch_tuple(stmt)
    # 计数器
    num = 0
    while (res):
        num += 1
        print("第" + str(num) + "行")
        # print(res)
        # for key,item in res:
        # print()
        key = ','.join(str(k) for k in res.keys())
        val = ','.join(
            '\'' + str(v) + '\''
            if isinstance(v, str)
            # or isinstance(v,unicode)
            # or isinstance(v,datetime.datetime)
            else str(v)
            for v in res.values())
        # print(key)
        # print(val)
        ins_str = "insert into %s (%s) values (%s);" % (tab_name, key, val)
        with open(file_name, 'a') as file:
            file.write(ins_str + "\n")
        file.close()
        # res=ibm_db.fetch_tuple(stmt)
        # res = ibm_db.fetch_both(stmt)
        res = ibm_db.fetch_assoc(stmt)
    print(("%s生成完成, 共%s条数据") % (tab_name, num))
    # 提交事务
    ibm_db.commit(conn)
except Exception as e:
    # 回滚事务
    print(e)
    ibm_db.rollback(conn)
finally:
    # 关闭数据库连接
    ibm_db.close(conn)
