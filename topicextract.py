#coding:utf-8
import jieba
import jieba.analyse


def getTopicWords(input_sentences):

    print("="*25, "get topic words--textrank ---- start", "="*25)
    # 基于TextRank算法的关键词抽取
    keywords = jieba.analyse.textrank(input_sentences, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
    
    keywords_list = []
    for item in keywords:
        print(item[0],item[1])
        keywords_list.append(item[0])

    return keywords_list
