#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9

# 需先添加i包 
# pip install flask
# pip install flask_cors

from flask import Flask, abort, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

# 测试数据暂时存放
CORS(app, resources=r'/*') 
@app.route('/fun_add/', methods=['POST'])
def add_task():
    if not request.json or 'a' not in request.json or 'b' not in request.json:
        abort(400)
    x = int(request.json['a'])
    y = int(request.json['b'])
    return jsonify({'result': x + y})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5000, debug=True)
