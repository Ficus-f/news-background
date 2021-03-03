# -*- coding:utf-8 -*-

import requests
from lxml import etree
from urllib.parse import quote

def search_book(word):
    input_word = quote(word)
    url = "http://search.dangdang.com/?key=" + input_word + "&act=input"
    html = requests.get(url)
    etree_html = etree.HTML(html.text)
    content_ul_li_a = etree_html.xpath('//*[@id="component_59"]/li/a')
    i = 0
    word_books_list = []
    for each in content_ul_li_a:
        if i < 10:
            word_books_list.append(each.attrib['title'])
            i += 1
        else:
            break
    return word_books_list

