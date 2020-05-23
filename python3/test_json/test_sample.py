import json

# Python 字典类型转换为 JSON 对象
data = { "checksum": "ab0160f0e20bcc33180d002c3dd2a327",
            "roots": {
                "bookmark_bar": {
                    "children": [{
                        "date_added": "13184397381386565",
                        "id": "24",
                        "meta_info": {
                            "last_visited_desktop": "13202371654400597"
                        },
                        "name": "ext",
                        "sync_transaction_version": "770",
                        "type": "url",
                        "url": "chrome://extensions/"
                    }, {
                        "date_added": "13186477216183000",
                        "id": "15",
                        "meta_info": {
                            "last_visited_desktop": "13198488131734465"
                        },
                        "name": "快搜",
                        "sync_transaction_version": "543",
                        "type": "url",
                        "url": "http://search.chongbuluo.com/"
                    }
                    ]
                    }
                    }
                    }
# data = {
#     "fontFamily": "微软雅黑",
#     "fontSize": 12,
#     "BaseSettings": {
#         "font": 1,
#         "size": 2
#     }
# }
# print("Python 原始数据：", repr(data))
# print("JSON 对象：", json_str)
dic = {}


def json_txt(dic_json):
    if isinstance(dic_json, dict):  #判断是否是字典类型isinstance 返回True false
        print("BEGIN")
        for key in dic_json:
            if isinstance(dic_json[key], dict):  #如果dic_json[key]依旧是字典类型
            #     # print("****key--：%s value--: %s" % (key, dic_json[key]))
            #     # json_txt(dic_json[key])
            #     # dic[key] = dic_json[key]
                json_txt(dic_json[key])
            # else:
            #     if (key == 'name' and dic_json['url']):
            #         print("YES:" + dic_json['url'])
            print("****key--：%s value--: %s" % (key, dic_json[key]))
    else:
        print("begin")


json_str = json.dumps(data)
# print(json_str)
data2 = json.loads(json_str)
# print(data2)
json_txt(data2)