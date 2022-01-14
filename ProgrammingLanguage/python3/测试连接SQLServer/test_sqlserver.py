# _*_coding:utf-8_*_
import pymssql

conn = pymssql.connect(host='10.16.16.17',database='master',user='iqdsdb2',password='Iqds_bkd')
cur = conn.cursor()
if not cur:
    raise(NameError,"connect database fails") 
else:
    cur.execute("select getdate()")
    data = cur.fetchall()

    if data :
        print("ok")
        for i in data:
            print(i)
    else:
        print("fail")
    conn.close()