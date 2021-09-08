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
from werkzeug.sansio.response import Response
import xmltodict
import uuid
import time
from flask import Flask, abort, request, jsonify
from zeep import Client
from xml.dom.minidom import parseString
 
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

Webservice_url="http://127.0.0.1/hmiDataGate/HmiDataGate.asmx?WSDL"
app = Flask(__name__)

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
    result = client.service.GetHmiData(ReqList)
    xml_str = '<result>' + result + '</result>'
    # ����xmlתjson�ĺ���
    return (xml_to_json(xml_str))
    
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
    # tasks = []
    # for TagList in TagLists:
    #     Tags = TagList.getElementsByTagName("Tag")
    #     for Tag in Tags:
    #         if Tag.hasAttribute("Name"):
    #             task = {
    #                 'Name': Tag.getAttribute("Name"),
    #                 'Value': Tag.getAttribute("Value")
    #             }
    #             if Tag.hasChildNodes(): # �ж��Ƿ�Ϊ��¼������
    #                 Dats = Tag.getElementsByTagName("Dat")
    #                 for Dat in Dats: # ������Щ����--����֪����¼���ṹ���޷���������
    #                     task = {
    #                         'Name': Dat.getAttribute("Name"),
    #                         'Value': Dat.getAttribute("Value")
    #                     }
    #                 tasks.append(task)
    #             # print ("Name: %s" % Tag.getAttribute("Name"))
    #             # print ("Value: %s" % Tag.getAttribute("Value"))
    # return jsonify(tasks)




# �����ʽ    {"msgList":[{"id":"MSG3301","timeout":60,"reply":true,"data":[{"EntryThk":"30","BarTemp":"1000","TimeOf1To2":"20"}]}]}
@app.route('/webservice/sendMessage', methods=['POST'])
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
        #    print ('======key========:'+key+"************value******"+datas[key])
            Dat += key +'''="'''+ datas[key] +'''" '''
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
    ReqList = '''<ReqDat><MsgList><Msg Id="''' + str(msg_id) + '''" Ticket="''' + str(Ticket) + '''" Timeout="0" Reply="0"/></MsgList></ReqDat>'''
    # print (ReqList)
    code = 0
    result = client.service.GetHmiData(ReqList)
    if result != None:
        code = 200
    else:
        i=1
        while (result == None ):
            time.sleep(0.5) # ����1��
            i += 1
            result = client.service.GetHmiData(ReqList)
            # print (result)
            if result != None:
                code = 200
            if i > 20:     # ��i����10ʱ����ѭ��
                break
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
    
    xml_str = '<data>' + result + '</data>'
    # ����xmlתjson�ĺ���
    # return (xml_to_json(xml_str))
    result_json = (xml_to_json(xml_str))
    # print ("result  is " +  result_json)
    results = json.loads(result_json)
    data = results["data"]["MsgList"]["Msg"]["Dat"]
    # print(data)
    datalist = []
    datalist.append(results["data"]["MsgList"]["Msg"]["Dat"])
    msg_res = {"id":results["data"]["MsgList"]["Msg"]["Id"],"ticket":results["data"]["MsgList"]["Msg"]["Ticket"],"dataList":datalist}
    msgList = []
    msgList.append(msg_res)
    resp1 = {'code': code,'data':{"tagList":None,"msgList": msgList }}
    print (resp1)
    resp = jsonify(resp1)
    return resp
   


if __name__ == "__main__":
    # ��host����Ϊ0.0.0.0���������û�Ҳ���Է��ʵ��������
    # app.run(host="0.0.0.0", port=9999, debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=9999)
