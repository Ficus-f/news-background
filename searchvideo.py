#coding:utf-8
import requests
from bs4 import BeautifulSoup
import xlwt

## 在b站中搜索
def search_entity_in_b(word):
    response = []
    url_to_b = "https://search.bilibili.com/all?keyword="
    url = url_to_b + word
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, "html.parser")
    links = soup.find_all('a', {"class":"title"})
    for link in links:
        # 暂且只取10条
        if len(response) == 10:
            break
        # entity_link = {}
        # entity_link[link['title']] = link['href'][2:]
        entity_link = []
        entity_link.append(link['title'])
        entity_link.append(link['href'][2:])
        response.append(entity_link)
    return response
