# #python获取webservice，已实现获取标准webservice
# # https://docs.python-zeep.org/en/master/

# from zeep import Client
# AOurl="http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl"
# client = Client(AOurl)
# # print(client)
# ProvinceName = "四川"
# result = client.service.getSupportCity(ProvinceName)
# print(result)
# # f = open('2.xml','rt',encoding='GB2312')
# # s=f.read()
# # response=client.service.DEMO1(s)
# # print(response)
# # f.close()

# #需要进一步测试xml通讯内容-----ok
from zeep import Client
AOurl="http://127.0.0.1/hmiDataGate/HmiDataGate.asmx?WSDL"
client = Client(AOurl)
# print(client)
ReqList = '''<ReqDat><TagList><Tag Name="test2" TS="0"/></TagList></ReqDat>'''
result = client.service.GetHmiData(ReqList)
print(result)
