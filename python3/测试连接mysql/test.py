import pymysql

# 打开数据库连接 connect("ip","用户名","密码","数据库名") 区分大小写
db = pymysql.connect("192.168.142.136", "root", "123456", "test001")

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute()方法执行sql语句查询
# cursor.execute("select VERSION()")

# # 使用fetchone()方法获取单条数据
# data = cursor.fetchone()
# print("the data : %s " % data)

# # 使用预处理语句创建表
#====================================== SQL 创建表start========================================
# sql = "CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"
# cursor.execute(sql)
#====================================== SQL 创建表end========================================

# # SQL 插入语句
#====================================== SQL 插入语句start========================================
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Macbook', 'Jojo', 23, 'M', 4000)"
# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
#====================================== SQL 插入语句end========================================

# SQL 查询语句
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

# #====================================== SQL 查询语句start========================================
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#                (fname, lname, age, sex, income ))
# except:
#     print("Error: unable to fetch data")
# #====================================== SQL 查询语句end========================================

# #====================================== SQL 更新语句start========================================
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
# #====================================== SQL 更新语句end========================================

# SQL 删除语句
# # #====================================== SQL 删除语句start========================================
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (27)
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交修改
#     db.commit()
#     print("delete ok!")
# except:
#     # 发生错误时回滚
#     db.rollback()
# # #====================================== SQL 删除语句end========================================

#关闭数据库连接
db.close()