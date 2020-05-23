# 该实例可以获取绝对路径下某文件，并解析   待完成：解析json

import json


def loadjsonfile():
    f = open("FrontEnd\解析json文件数据并保存到本地\Bookmarks.json", encoding='utf-8')
    # f = open(
    #     "H:\\Users\\Administrator\\AppData\\Local\\Microsoft\\Edge Dev\\User Data\\Default\\Bookmarks",
    #     encoding='utf-8'
    # )  # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    Bookmarks_file = json.load(f)
    return Bookmarks_file


# t['name']  # 注意多重结构的读取语法
#遍历json文件所有的key对应的value
dic = {}


def json_txt(dic_json):
    if isinstance(dic_json, dict):  #判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  #如果dic_json[key]依旧是字典类型
                print("****key--：%s value--: %s" % (key, dic_json[key]))
                # json_txt(dic_json[key])
                # dic[key] = dic_json[key]
                dic[key] = json_txt(dic_json[key])
            else:
                if (key == 'name' and dic_json['url']):
                    print(dic_json['url'])
                print("****key--：%s value--: %s" % (key, dic_json[key]))


t = loadjsonfile()
print(t)
# json_txt(t)
# print(final_json)