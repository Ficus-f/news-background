#coding:utf-8
import jieba
import jieba.analyse
from urllib.parse import quote
import urllib
import urllib.request
import json
import numpy as np


def search_kg_entity(words_list):
    response_entity = {}
    for word in words_list:
        input_entity = quote(word)
        # 输入实体名，返回对应实体
        input_url_entity = 'http://shuyantech.com/api/cndbpedia/ment2ent?q='
        url_entity = input_url_entity + input_entity
        _response_entity = urllib.request.urlopen(url_entity)
        _response_entity = _response_entity.read().decode('utf-8')
        _response_entity = json.loads(_response_entity)
        response_entity[word] = _response_entity['ret']
    return response_entity


# 输入1个单词，返回该词相关信息列表
def search_kg_triple(word):
    input_entity = quote(word)
    # 输入实体名，返回实体全部的三元组知识
    input_rul_knowledge = 'http://shuyantech.com/api/cndbpedia/avpair?q='
    url_knowledge = input_rul_knowledge + input_entity
    _response_knowledge = urllib.request.urlopen(url_knowledge)
    _response_knowledge = _response_knowledge.read().decode('utf-8')
    _response_knowledge = json.loads(_response_knowledge)
    return _response_knowledge['ret']
