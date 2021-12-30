# 该实例能获取所有的json数据，拼成一个数组类型


from __future__ import print_function
import json


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


if __name__ == "__main__":
    # sJOSN = ''
    sJOSN ={ "checksum": "ab0160f0e20bcc33180d002c3dd2a327",
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
    json_str = json.dumps(sJOSN)
    sValue = json.loads(json_str)
    for i in dict_generator(sValue):
        print(i)
            # print('.'.join(i[0:-1]), ':', i[-1])