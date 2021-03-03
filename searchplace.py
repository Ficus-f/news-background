# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from xpinyin import Pinyin


def search_util(url):
    # 发送请求，不允许跳转
    r = requests.get(url, allow_redirects=False)
    # 如果返回的结果不是200，则返回空
    if r.status_code != 200:
        return ''
    r_text = r.text
    soup = BeautifulSoup(r_text, "html.parser")
    try:
        content = soup.find('div', {'class':'mdd-tab-wordbox'}).text
        response = content.strip()
    except:
        response = ''
    return response


def cut_content_len(content, url):
    if len(content) > 400:
        content = content[:400] + '...'
    tmp_list = []
    tmp_list.append(content)
    tmp_list.append(url)
    return tmp_list


def search_place_info(word):
    '''
    @param: the name of place
    @return: 如果没有找到相关信息，则返回None；若找到，则返回 当地娱乐、美食、历史、民俗、介绍
    '''
    # 将单词转化为拼音
    pinyin = Pinyin()
    word_pinyin = pinyin.get_pinyin(word, '')
    # 开始搜索当地娱乐、美食、历史、民俗、介绍
    url_entertainment = 'http://' + word_pinyin + '.alltrip.cn/entertainment#mdd-link-dw'
    url_food = 'http://' + word_pinyin + '.alltrip.cn/food#mdd-link-dw'
    url_history = 'http://' + word_pinyin + '.alltrip.cn/history#mdd-link-dw'
    url_folkways = 'http://' + word_pinyin + '.alltrip.cn/folkways#mdd-link-dw'
    url_introduce = 'http://' + word_pinyin + '.alltrip.cn/introduce#mdd-link-dw'
    # 封装成为字典返回
    response = {}
    response['entertainment'] = cut_content_len(search_util(url_entertainment), url_entertainment)
    response['food'] = cut_content_len(search_util(url_food), url_food)
    response['history'] = cut_content_len(search_util(url_history), url_history)
    response['folkways'] = cut_content_len(search_util(url_folkways), url_folkways)
    response['introduce'] = cut_content_len(search_util(url_introduce), url_introduce)
    # 如果返回为空，说明没有找到该地名相关的信息，则返回None
    if response['entertainment'] == response['food'] == response['history'] == response['folkways'] == response['introduce'] == '': 
        return None
    return response


# 测试
if __name__ == '__main__':
    word = '中国上海'
    response = search_place_info(word)
    print(response)