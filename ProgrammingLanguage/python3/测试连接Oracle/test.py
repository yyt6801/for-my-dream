import cx_Oracle
conn = cx_Oracle.connect('ANSTEEL/ANSTEEL@10.151.18.165:1521/NERCAR')
print("OK")
curs = conn.cursor()
sql = 'select * from product_component_version'
curs.execute(sql)

for result in curs:
    print(result)

curs.close()
conn.close()