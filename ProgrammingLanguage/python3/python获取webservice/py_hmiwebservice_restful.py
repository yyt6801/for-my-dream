#-*- coding: gb2312 -*-
#todo:ʵ��һ��restful server ����http client����
#�����������ݣ�ȥ����webservice�������ؽ�����ظ�http client
# 1. ʵ��getHmiData�ӿڣ���ȡ��������(��ͨ����and��¼������)
# 2. ʵ�ַ�����ϢsendMassage�Ƚӿڣ� ��дsendMessageNew��������ȡ��׼����ֵ
# 3. ʵ�����ݿ��ѯ��ز���

# from zeep import Client
# AOurl="http://127.0.0.1/hmiDataGate/HmiDataGate.asmx?WSDL"
# client = Client(AOurl)
# tag_name = "test"
# ReqList = '''<ReqDat><TagList><Tag Name="'''+tag_name+ '''" TS="0"/></TagList></ReqDat>'''
# result = client.service.GetHmiData(ReqList)
# print(result)


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from flask import Flask

# # Flask��ʼ����������ʹ����İ����������ʼ����ʽ�ǹٷ��Ƽ��ģ��ٷ����ͣ�http://flask.pocoo.org/docs/0.12/api/#flask.Flask
# app = Flask(__name__)


# if __name__ == "__main__":
#     # �����ǲ�̫�Ƽ���������ʽ������ֻ������ʾ�ã��ٷ�������ʽ�μ���http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
#     app.run(debug=True)


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from flask import Flask, abort, request, jsonify

# app = Flask(__name__)

# # ����������ʱ���
# tasks = []

# @app.route('/add_task/', methods=['POST'])
# def add_task():
#     if not request.json or 'id' not in request.json or 'info' not in request.json:
#         abort(400)
#     task = {
#         'id': request.json['id'],
#         'info': request.json['info']
#     }
#     tasks.append(task)
#     return jsonify({'result': 'success'})


# @app.route('/get_task/', methods=['GET'])
# def get_task():
#     if not request.args or 'id' not in request.args:
#         # û��ָ��id�򷵻�ȫ��
#         return jsonify(tasks)
#     else:
#         task_id = request.args['id']
#         task = filter(lambda t: t['id'] == int(task_id), tasks)
#         return jsonify(task) if task else jsonify({'result': 'not found'})


# if __name__ == "__main__":
#     # ��host����Ϊ0.0.0.0���������û�Ҳ���Է��ʵ��������
#     app.run(host="0.0.0.0", port=9999, debug=True)




# -------------------------��ʼʵ��----------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask.json import tag
from werkzeug.sansio.response import Response
import xmltodict
import uuid
import time
from flask import Flask, abort, request, jsonify
from flask_cors import CORS 
from zeep import Client

import configparser
import os
from xml.dom.minidom import parseString

import cx_Oracle
 
def xml_to_json(xml_str):
    # parse�ǵ�xml������
    xml_parse = xmltodict.parse(xml_str, attr_prefix='', cdata_key='') # ͨ������������ȥ��@��# (���ڱ�ʾ���Ժ��ı��ڵ�ʹ���Ǵ�Ԫ�����ֿ���)
    # json��dumps()�ǽ�dictת����json��ʽ,loads()�ǽ�jsonת����dict��ʽ��
    # dumps()������ident=1,��ʽ��json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str
# jsonתxml����
def json_to_xml(json_str):
    # xmltodict���unparse()jsonתxml
    # ����pretty �Ǹ�ʽ��xml
    xml_str = xmltodict.unparse(json_str, pretty=1)
    return xml_str

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")
conf = configparser.ConfigParser() # ����������� 
conf.read(cfgpath, encoding="utf-8")  # python3 # ��ini�ļ�
items = conf.items('webservice')
Webservice_url=""
Webservice_url=str(items[0][1])
print(Webservice_url)  

#ANSTEEL/ANSTEEL@10.151.18.165:1521/NERCAR 
oracle_username = conf.get("oralce","username")
oracle_host = conf.get("oralce","host")
oracle_port = conf.get("oralce","port")
oracle_password = conf.get("oralce","password")
oracle_db = conf.get("oralce","db")
ora_url = oracle_username + '/' + oracle_username + '@'+oracle_host+":"+oracle_port+'/'+oracle_db
print(ora_url)  

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app, supports_credentials=True)  # ���ÿ���

@app.route('/test')
def hello_world():
    return "Welcome!   Python_hmiwebservice is  running..."

# //����ok
# <TagList><Tag Name="Tag001" TS="0"/></TagList>
# �����ʽ    {"msgs":[],"tags":[{"name":"Z.1.ZONE1.TCM3_S1.ACT_SPEED","ts":"0"},{"name":"Z.1.ZONE1.TCM3_S5.GAP_ACT","ts":"0"}]}
@app.route('/webservice/getHmiData', methods=['POST'])
def getHmiData():
    print(request.json)
    if not request.json or 'msgs' not in request.json or 'tags' not in request.json:
        abort(400)
    tags_data = []
    tags_data = request.json['tags'] #[{'name': 'test', 'ts': '0'}, {'name': 'test2', 'ts': '0'}]
    tag_list = ""
    for tags in tags_data:       
        # print (tags['name'])
        tag_list += '''<Tag Name="'''+tags['name']+ '''" TS="0"/>'''

    client = Client(Webservice_url)
    ReqList = '''<ReqDat><TagList>''' + tag_list + '''</TagList></ReqDat>'''
    # print (ReqList)
    code = 0
    result = client.service.GetHmiData(ReqList)
    if result != None:
        code=200
    xml_str = '<data>' + result + '</data>'
    # ����xmlתjson�ĺ���
    # return (xml_to_json(xml_str))      #������Ӧ�ý����������и�ʽ��һ����Ϊ����֮ǰ�ӿڣ�ʹ������ƴ��
    # {
    #  "data": {
    #   "TagList": {
    #    "Tag": [
    #     {
    #      "Name": "C",
    #      "TS": "132332226832889690",
    #      "Value": "1.068"
    #     },
    #     {
    #      "Name": "FMRsFlag",
    #      "TS": "132745119208578183",
    #      "Dat": []
    #     }
    #    ]
    #   },
    #   "MsgList": null
    #  }
    # }
    #ǰ���÷���res.data.tagList[0].value  ��¼�� res.data.tagList[51].dataList
    # {"code":0,"msg":"","extraMsg":"","data":{"tagList":[{"name":"C","ts":"132332226832889690","value":"1.068","dataList":null},{"name":"FMRsD","ts":"132745119208588040","value":null,"dataList":[{"d":"76.487"},{"d":"27.042"},{"d":"22.715"},{"d":"19.176"},{"d":"16.464"},{"d":"19.746"},{"d":"18.169"}]}],"msgList":null}}
    result_json = (xml_to_json(xml_str))
    # print ("result  is " +  result_json)
    results = json.loads(result_json)
    tagList = {}
    tagList = results["data"]["TagList"]
    if (tagList != None) :
        results_Tag = []
        results_Tag = tagList["Tag"]
        if (isinstance(results_Tag,list)) :
            tagLists = []
            for Tag in results_Tag:
                print (Tag)
                if "Value" in Tag:
                    tag = {"name":Tag["Name"],"ts":Tag["TS"],"value":Tag["Value"]}
                    tagLists.append(tag)
                if "Dat" in Tag:
                    tag = {"name":Tag["Name"],"ts":Tag["TS"],"dataList":Tag["Dat"]}
                    tagLists.append(tag)
        else:
            tagLists = results_Tag
    else:
        tagLists = None
    resp1 = {'code': code,'data':{"tagList":tagLists,"msgList": None }}
    print (resp1)
    resp = jsonify(resp1)
    return resp

    # ������Ľ��xmlת��Ϊjson�������Թ�ֱ��ʹ��
    # <TagList>
    #     <Tag Name="test" TS="132533330707268108" Value="123"/>
    #     <Tag Name="test2" TS="132066355506925179" Value="0.123"/>
    #     <Tag Name="testrec" TS="132164530356104234">
    #         <Dat a="JF302U0R" b="JF302U0R" c="JF302U0R" d="JF302U0R"/>
    #         <Dat a="JF302U0R" b="JF3adfadfad" c="JF302U0R" d="JF302U0R"/>
    #         <Dat a="JF302U0R" b="JF302U0R" c="JF302U0R" d="JF302U0R"/>
    #     </Tag>
    # </TagList>
    # <MsgList></MsgList>

    # ʹ��minidom�������� XML �ĵ�
    # print(xml_to_json(xml_str))
    # xml_dom = parseString(xml_str)
    # TagLists = xml_dom.getElementsByTagName("TagList")
    # tagList = []
    # dataList = []
    # for TagList in TagLists:
    #     Tags = TagList.getElementsByTagName("Tag")
    #     for Tag in Tags:
    #         if Tag.hasAttribute("Name"):
    #             task = {
    #                 'Name': Tag.getAttribute("Name"),
    #                 'Value': Tag.getAttribute("Value")
    #             }
    #             if Tag.hasChildNodes(): # �ж��Ƿ�Ϊ��¼������
    #                 # Dats = Tag.getElementsByTagName("Dat")
    #                 task["dataList"] = Tag["Dat"]
    #             else:
    #                 task["value"] = Tag["Value"]
                    
    #             # print ("Name: %s" % Tag.getAttribute("Name"))
    #             # print ("Value: %s" % Tag.getAttribute("Value"))
    #         tagList.append(task)
    # return jsonify(tagList)




# �����ʽ    {"msgList":[{"id":"MSG3301","timeout":60,"reply":true,"data":[{"EntryThk":"30","BarTemp":"1000","TimeOf1To2":"20"}]}]}
@app.route('/webservice/sendMessageNew', methods=['POST'])
def sendMessage():
    print(request.json)
    datas = ""
    if not request.json or 'msgList' not in request.json :
        abort(400)
    req_data = json_to_xml(request.json)
    # print (req_data) 
    msgList_data = []
    msgList_data = request.json['msgList'] #[{"id":"MSG1401","timeout":60,"reply":true,"data":[{"EntryThk":"30","BarTemp":"1000","TimeOf1To2":"20"}]}]
    msg_id = msgList_data[0]["id"]
    msg_timeout = msgList_data[0]["timeout"]
    msg_reply = "1" if msgList_data[0]["reply"] == True else "0"
    msg_data = msgList_data[0]["data"]
    Dat = " "
    for datas in msg_data:
        Dat += '''<Dat '''
        for key in  datas :
            # print ('======key========:'+str(key)+"************value******"+str(datas[key]))
            Dat += str(key) +'''="'''+ str(datas[key]) +'''" '''
        Dat += ''' />'''

    # print (Dat) 
    # ��������xml
    # //����ok
    # <MsgList><Msg Id="MSG3000" Ticket="132164530356104234" Timeout="0" Reply="0"><Dat x="30" y="1000"/></Msg></MsgList>
    # Ticket = uuid.uuid4()
    Ticket = uuid.uuid4().hex[16:]
    # print (Ticket) 
    DatXml = '''<MsgList> <Msg Id="''' + str(msg_id) + '''" Ticket="'''+ str(Ticket) +'''" Timeout="'''+ str(msg_timeout) +'''" Reply="'''+ str(msg_reply) +'''"> '''+ Dat +'''</Msg></MsgList>'''
    # print (DatXml) 
    client = Client(Webservice_url)
    result = client.service.SendData(DatXml)
    # print (result) # ��������xml

    #�ٴθ���ID��ticket����getHMIData������ȡ����ֵ
    #<MsgList><Msg Id="MSG3000" Ticket="132164530356104234" Timeout="0" Reply="0"><Dat x="30" y="1000"/></Msg></MsgList>
    ReqList = '''<ReqDat><MsgList><Msg Id="''' + str(msg_id) + '''" Ticket="''' + str(Ticket) + '''" Timeout="'''+ str(msg_timeout) +'''" Reply="0"/></MsgList></ReqDat>'''
    # print ("ReqList"+ReqList)
   
    #�����ؽ����װΪ�����ʽ
    # {
    #     "TagList": null,
    #     "MsgList": {
    #         "Msg": {
    #             "Id": "MSG3000",
    #             "Ticket": "91e652a925c07a73",
    #             "Dat": {
    #               "ID": "PartCanRecord",
    #               "INFO": "\u6279\u91cf\u540a\u9500\u6210\u529f"
    #             }
    #         }
    #     }
    # }
    #{"code":0,"msg":"","extraMsg":"","data":{"tagList":null,"msgList":[{"id":"MSG2020","ticket":"1028f102-d72e-4857-b485-f62ecf1fe182","dataList":[{"ID":"ModCal","INFO":"ģ�����ɹ�","e":"313.535"}]}]}}
    

    code = 0
    # time.sleep(0.5) # ����1��
    result = client.service.GetHmiData(ReqList)
    xml_str = '<data>' + result + '</data>'
    # ����xmlתjson�ĺ���
    # return (xml_to_json(xml_str))
    result_json = (xml_to_json(xml_str))
    # print ("result  is " +  result_json)
    results = json.loads(result_json)
    MsgList = {}
    MsgList = results["data"]["MsgList"]
    i=1
    while (MsgList == None ):
        time.sleep(0.3) # ����1��
        result = client.service.GetHmiData(ReqList)
        xml_str = '<data>' + result + '</data>'
        result_json = (xml_to_json(xml_str))
        # print ("result  is " +  result_json)
        results = json.loads(result_json)
        MsgList = results["data"]["MsgList"]
        i += 1
        # print (result)
        if i > 30:     # ��i����10ʱ����ѭ��
            break
    if (MsgList != None) :
        code = 200
        data = results["data"]["MsgList"]["Msg"]["Dat"]
        datalist = []
        if (isinstance(data,list)) :
            datalist = data
        else:
            datalist.append(data)
        msg_res = {"id":results["data"]["MsgList"]["Msg"]["Id"],"ticket":results["data"]["MsgList"]["Msg"]["Ticket"],"dataList":datalist}
        MsgList = []
        MsgList.append(msg_res)
    else:
        MsgList = None
    resp1 = {'code': code,'data':{"tagList":None,"msgList": MsgList }}
    print (resp1)
    resp = jsonify(resp1)
    return resp
   
#/common/findData    {"key":"query_efficiency","list":[{"@where":""}]}
#{"key":"oracle_template","list":[{"@sql":"select a.* from frsa_setpoints_tensions_new a"}]}
#{"msg":"�������ݽӿڳɹ�","status":2000,"data":[{"F_QUENCH":11.3,"F_BRIDLE3":13.4,"F_RAPID_COOL":7.8,"WIDTH":1600,"F_SOAK":5.5,"STGR_GROUP":".TENS-0","F_HEAT3":5.5,"F_HEAT2":7,"F_HEAT1":8.6,"F_FIN_COOL":7.3,"F_OVERAGING3":5.7,"F_OVERAGING1":5.7,"F_OVERAGING2":5.7,"SPEC":"00716","THICKNESS":0.7,"MTIME":"2021-04-01T02:56:54.000+0000"}],"count":0}
@app.route('/common/findData', methods=['POST'])
def findData():
    print(request.json)
    if not request.json or 'key' not in request.json or 'list' not in request.json:
        abort(400)
    datalist = []
    conn = cx_Oracle.connect(ora_url)
    curs = conn.cursor()
    sql = request.json['key']
    res = curs.execute(sql)
    print(res)
    code = "ʧ��"
    if res == None:
        conn.commit()  # �ύ���
        code = "�������ݳɹ�"
    else:
        for result in curs:
            datalist.append(result)
        code = "�������ݽӿڳɹ�"
    curs.close()
    conn.close()
    res = {'msg': code,"status":2000,'data':datalist,"count":0}
    resp = jsonify(res)
    return resp

if __name__ == "__main__":
    # ��host����Ϊ0.0.0.0���������û�Ҳ���Է��ʵ��������
    # app.run(host="0.0.0.0", port=9999, debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=9999)
