#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9

from flask import Flask

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(host="0.0.0.0", port=5000, debug=True)
