#todo:实现一个restful server 监听http client请求
#解析请求内容，去请求webservice，将返回结果返回给http client
# 1. 实现getHmiData接口，获取变量数据(普通变量and记录集变量)
# 2. 实现发送消息sendMassage等接口， 改写sendMessageNew方法，获取标准返回值
# 3. 实现数据库查询相关操作

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

# # Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
# app = Flask(__name__)

# @app.route('/HelloWorld')
# def hello_world():
#     return "Hello World!"

# if __name__ == "__main__":
#     # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
#     app.run(debug=True)


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from flask import Flask, abort, request, jsonify

# app = Flask(__name__)

# # 测试数据暂时存放
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
#         # 没有指定id则返回全部
#         return jsonify(tasks)
#     else:
#         task_id = request.args['id']
#         task = filter(lambda t: t['id'] == int(task_id), tasks)
#         return jsonify(task) if task else jsonify({'result': 'not found'})


# if __name__ == "__main__":
#     # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
#     app.run(host="0.0.0.0", port=9999, debug=True)




# -------------------------开始实现----------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import xmltodict
from flask import Flask, abort, request, jsonify
from zeep import Client
from xml.dom.minidom import parseString
 
def xml_to_json(xml_str):
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str, attr_prefix='', cdata_key='') # 通过两参数可以去掉@和# (用于表示属性和文本节点使它们从元件区分开来)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str
# json转xml函数
def json_to_xml(json_str):
    # xmltodict库的unparse()json转xml
    # 参数pretty 是格式化xml
    xml_str = xmltodict.unparse(json_str, pretty=1)
    return xml_str

Webservice_url="http://127.0.0.1/hmiDataGate/HmiDataGate.asmx?WSDL"
app = Flask(__name__)
# 请求格式    {"msgs":[],"tags":[{"name":"Z.1.ZONE1.TCM3_S1.ACT_SPEED","ts":"0"},{"name":"Z.1.ZONE1.TCM3_S5.GAP_ACT","ts":"0"}]}
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
    # 定义xml转json的函数
    return (xml_to_json(xml_str))
    
    # 把请求的结果xml转化为json，返回以供直接使用
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
    # 使用minidom解析器打开 XML 文档
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
    #             if Tag.hasChildNodes(): # 判断是否为记录集变量
    #                 Dats = Tag.getElementsByTagName("Dat")
    #                 for Dat in Dats: # 这里有些问题--（不知道记录集结构）无法继续解析
    #                     task = {
    #                         'Name': Dat.getAttribute("Name"),
    #                         'Value': Dat.getAttribute("Value")
    #                     }
    #                 tasks.append(task)
    #             # print ("Name: %s" % Tag.getAttribute("Name"))
    #             # print ("Value: %s" % Tag.getAttribute("Value"))
    # return jsonify(tasks)

# 请求格式    {"msgList":[{"id":"MSG3301","timeout":60,"reply":true,"data":[{"EntryThk":"30","BarTemp":"1000","TimeOf1To2":"20"}]}]}
@app.route('/webservice/sendMessage', methods=['POST'])
def sendMessage():
    print(request.json)
    datas = ""
    if not request.json or 'msgList' not in request.json :
        abort(400)
    req_data = json_to_xml(request.json)
    msgList_data = []
    msgList_data = request.json['msgList'] #[{"id":"MSG1401","timeout":60,"reply":true,"data":[{"EntryThk":"30","BarTemp":"1000","TimeOf1To2":"20"}]}]
    msg_id = msgList_data[0]["id"]
    msg_data = msgList_data[0]["data"]
    datas = msg_data[0]
    # for datas in msg_data:
    #     for tag_names in datas:
    #         tag_names[]

    # DatXml = '''<DatXml>''' + req_data + '''</DatXml>'''
    print (req_data) # 请求内容xml

    client = Client(Webservice_url)
    result = client.service.SendData(req_data)
    print (result) # 请求内容xml
    xml_str = '<result>' + result + '</result>'
    # 定义xml转json的函数
    return (xml_to_json(result))
   


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=9999, debug=True)
