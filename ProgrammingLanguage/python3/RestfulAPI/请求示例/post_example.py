#!utf-8
import http.client
import json

conn = http.client.HTTPConnection("170.0.200.113", 8080)
payload = json.dumps({
   "extid": "H2110429600",
   "theme_group_id": "c621_pdoandpdi_sisteel"
})
headers = {
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': '170.0.200.113:8080',
   'Connection': 'keep-alive'
}
conn.request("POST", "/coldbigdata/tbDsjThemeData/find_model", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))