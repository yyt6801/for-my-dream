import cx_Oracle
import requests
import json
import time

# cx_Oracle.init_oracle_client(lib_dir=r"F:\Tools\instantclient_21_10")
cx_Oracle.init_oracle_client(lib_dir=r"D:\yyt\instantclient_21_10")
conn = cx_Oracle.connect('ORAINS/123456@10.151.18.211:1521/nercar')
print("OK")
coilno = ''
pos = 0
curs = conn.cursor()
# sql = '''select t.coilno,t.pos from tb_tcm2track_time t where t.tbflag =0 and t.enttime > to_date('2024-12-04 22:00:00','YYYY-MM-DD HH24:MI:SS') and t.pos not in (1,25,30,36,58,68,69,80,84,97,99,106) order by t.enttime asc '''
sql = '''select t.coilno,t.pos,enttime from tb_tcm2track_time t where t.tbflag =0 and t.enttime > to_date('2024-12-04 22:00:00','YYYY-MM-DD HH24:MI:SS') and t.pos in (10,104,105,107,108,109,110,111,32,35,40,523,524,533,534,59,7,70,72,76,81,88,9,92,94) order by t.enttime asc '''
curs.execute(sql)

for result in curs:
    print(result)
    # coilno, pos = result
    coilno = result[0]
    pos = int(result[1])
    if coilno :
        # 通过 http://10.16.1.249:8090/coldbigdata/curveData/toGetCurveData 接口发送触发板形计算消息
        # {
        #     "volumeNo":"L12407271600",
        #     "pos" : "110",
        #     "line" : "PLCTM"
        # }
        payload = json.dumps({
            "coilno": coilno,
            "pos": pos,
            "line_name": "PLTCM2"
        })
        # print(payload)
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://10.151.18.226:8090/coldbigdata/curveData/toGetCurveData', headers=headers,data= payload)
        print("send extid=" + coilno +" pos=" +str(pos))
        print('res:', response.text)
        # if response.status_code == 200:
        #     print('Success:', response.json())
        # else:
        #     print('Failed:', response.status_code)
    time.sleep(1)
curs.close()
conn.close()