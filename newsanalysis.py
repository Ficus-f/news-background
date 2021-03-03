# -*- coding:utf-8 -*-
import requests
import json
import jieba
import jieba.analyse

import topicextract
import searchkg
import searchvideo
import searchbook

# =========左边列==========
# 获取新闻列表函数
def get_news():
    """
    @param: null
    @returns: dict of news' title & abstract & url
        # response = {'message': 'success', 
        #             'data': [{"abstract":"...", "title":"...", "url":"..."},
        #             {"abstract":"...", "title":"...", "url":"..."},
        #             {"abstract":"...", "title":"...", "url":"..."},
        #             {"abstract":"...", "title":"...", "url":"..."},
        #             ...
        #            ]
    """
    response_news = {}
    response_news['message'] = 'success'
    url = "http://ic.snssdk.com/2/article/v25/stream/?count=20&min_behot_time=1504621638&bd_latitude=4.9E-324&bd_longitude=4.9E-324&bd_loc_time=1504622133&loc_mode=5&loc_time=1504564532&latitude=35.00125&longitude=113.56358166666665&city=%E7%84%A6%E4%BD%9C&lac=34197&cid=23201&iid=14534335953&device_id=38818211465&ac=wifi&channel=baidu&aid=13&app_name=news_article&version_code=460&device_platform=android&device_type=SM-E7000&os_api=19&os_version=4.4.2&uuid=357698010742401&openudid=74f06d2f9d8c9664"
    try:
        url_response = requests.get(url,timeout=(3,7)) #返回Response对象
        url_response.raise_for_status() #若状态码不是200，抛出HTTPError异常
    except:
        response_news['message'] = 'failure'
        print("newsanalysis.get_news: There is something wrong with url!")
        return response_news
    # 返回正常，解析新闻内容
    content = url_response.text
    content_json = json.loads(content)
    # 提取新闻中的url、title、abstract，装到_list列表中
    _list = [] # 存放新闻的列表
    for r in content_json['data']:
        _news_title_abstr_url = {}
        _news_title_abstr_url['title'] = r['title']
        _news_title_abstr_url['abstract'] = r['abstract']
        _news_title_abstr_url['url'] = r['url']
        _list.append(_news_title_abstr_url)
    # 将新闻放入到response中
    response_news['data'] = _list
    print("====newsanalysis.get_news success!====")
    return response_news
    

# 提取关键词函数 返回前20个关键词 封装成为字典返回
def extract_keywords(recv_data):
    response_keywords = {}
    response_keywords['message'] = 'success'
    # 如果传入数据不为空
    if recv_data:
        news_abstract = recv_data.decode()
        # 提取关键词 列表 ====start====
        keywords_list = topicextract.getTopicWords(news_abstract)
        print("====newsanalysis.extract_keywords success!====")
        response_keywords['data'] = keywords_list
    else:
        # 如果接收到的数据为空
        response_keywords['message'] = 'failure'
    return response_keywords


# 获取tfidf关键词、人名、地名、关键句子
'''
{
	'message': 'success',
	'data': {
		'booklist': [],
		'quotelist': [],
		'placelist': ['越南'],
		'namelist': ['俞正声'],
		'tfidflist': ['礼堂', '全国政协', '国会', '会见', '主席', '中央政治局常委', '下午', '中共'],
		'triplelist': []
	}
}
'''


# 传入的词在知识图谱中找到对应的三元组
def get_kgtriple(recv_data):
    response_kg = {}
    response_kg['message'] = 'success'
    # 如果传入数据不为空
    if recv_data:
        word = recv_data.decode()
        # 查找知识图谱 ====start====
        response_kg['data'] = searchkg.search_kg_triple(word)
        print("====newsanalysis.get_kgtriple success!====")
    else:
        # 如果接收到的数据为空
        response_kg['message'] = 'failure'
    return response_kg


# 传入词的视频链接
def get_video(recv_data):
    response_video = {}
    response_video['message'] = 'success'
    # 如果传入数据不为空
    if recv_data:
        word = recv_data.decode()
        # 查找知识图谱 ====start====
        response_video['data'] = searchvideo.search_entity_in_b(word)
        print("====newsanalysis.get_kgtriple success!====")
    else:
        # 如果接收到的数据为空
        response_video['message'] = 'failure'
    return response_video


# 传入词的相关书籍
def get_book(recv_data):
    response_book = {}
    response_book['message'] = 'success'
    # 如果传入数据不为空
    if recv_data:
        word = recv_data.decode()
        # 查找知识图谱 ====start====
        response_book['data'] = searchbook.search_book(word)
        print("====newsanalysis.get_book success!====")
    else:
        # 如果接收到的数据为空
        response_book['message'] = 'failure'
    return response_book


