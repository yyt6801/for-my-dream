import cx_Oracle
import http.client
import json
import time

conn = cx_Oracle.connect('xclzmes/xclzmes@10.16.3.66:1521/lzmesdb')
print("OK")
coil_no_out = ''
ent_time = '2023/6/6 16:00:00'
curs = conn.cursor()
sql = '''select t.coil_no_out,t.created+0 as create_time from pklroll_performance t WHERE t.created < to_date('2023/6/6 16:00:00', 'YYYY-MM-DD HH24:MI:SS') and t.created > to_date('2023/6/5 00:00:00', 'YYYY-MM-DD HH24:MI:SS') order by t.created desc'''
curs.execute(sql)

for result in curs:
    print(result)
    extid = result["coil_no_out"]
    if extid :
        # 通过 http://10.16.1.86:8088/HMI 接口发送触发板形计算消息
            conn = http.client.HTTPConnection("10.16.1.86", 8088)
            payload = json.dumps({
                "action": "send_msg",
                "body": {
                "msgId": 2030,
                "params": [
                [
                    {
                        "CoilNo": extid
                    }
                ]
                ],
                "sendTo": "paopian",
                "timeout": 2,
                "waitReply": True
                },
                "operator": "director",
                "terminal": "director"
            })
            headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': '10.16.1.86:8088',
            'Connection': 'keep-alive'
            }
            conn.request("POST", "/HMI", payload, headers)
            print("send 2030: extid="+extid)
            res = conn.getresponse()
            data = res.read()
            print(data)
    time.sleep(10)
curs.close()
conn.close()