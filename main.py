# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from flask import jsonify, abort, make_response
from flask_cors import cross_origin
import json

import newsanalysis


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello world!"

# =========左边列==========
# 获取新闻列表
@app.route('/api/getnewslist', methods=['GET', 'POST'])
def getnewslist():
    # 将字典形式的response转化为json格式，并返回
    return json.dumps(newsanalysis.get_news())


# 提取关键词
@app.route('/api/extractkeywords', methods=['POST'])
def extractkeywords():
    recv_data = request.get_data()
    return json.dumps(newsanalysis.extract_keywords(recv_data))
    

# =========右边列==========
# 查找知识图谱
@app.route('/api/getkgtriple', methods=['POST'])
def getkgtriple():
    recv_data = request.get_data()
    return json.dumps(newsanalysis.get_kgtriple(recv_data))


# 查找相关视频
@app.route('/api/getvideo', methods=['POST'])
def getvideo():
    recv_data = request.get_data()
    return json.dumps(newsanalysis.get_video(recv_data))


# 查找相关书籍
@app.route('/api/getbook', methods=['POST'])
def getbook():
    recv_data = request.get_data()
    return json.dumps(newsanalysis.get_book(recv_data))


if __name__ == "__main__":
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5000)