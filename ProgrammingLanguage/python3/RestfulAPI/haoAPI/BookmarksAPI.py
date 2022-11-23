# # -*- coding:utf-8 -*-
#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from USE_DB import DB  # 调用另一个python中的类和函数， from a import b    a.py不需要加.py
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources=r'/*')	# 注册CORS, "/*" 允许访问所有api


@app.route('/', methods=['GET'])
def hello():
    return "hello world!"

@app.route('/test', methods=['GET'])
def get_test():
    return "hello world!"

#获取数据库查询结果并返回
@app.route('/get_json', methods=['POST'])
def get_tasks():
    # with DB() as db:   通过调用DB()函数，把返回的数据给as后面的db
    with DB() as db:
        db.execute(
            '''SELECT * FROM TB_URL_COLLECTIONS  where username = 'test' order by URL_ID asc'''
        )
        # 获取所有记录列表
        results = db.fetchall()
        new_res = []
        for i in results:
            print(str(i))
            a = {}
            a["URL_ID"] = i["URL_ID"]
            a["URL"] = i["URL"]
            a["TITLE"] = i["TITLE"]
            a["NOTES"] = i["NOTES"]
            print(a)
            new_res.append(a)
        j_str = json.dumps(new_res, ensure_ascii=False)
        return  str(j_str)
    # return jsonify({'bookmarks': new_res})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {}
    return jsonify({'task': task})


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=81)