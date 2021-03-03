# news-background
By recommending relevant background information to users, we can help people better understand the misunderstanding caused by lack of relevant knowledge when reading news.


# 新闻的背景信息
新闻一般由凝练的语句组成，由于新闻播报的是最新资讯，故其中还很有可能包括新颖的词汇或名词。由于背景信息的缺少等因素，这些词汇和语句就会成为理解新闻的阻碍。很多平台通过大众可以接受并喜欢的方式，用文字，视频等形式来向大众介绍背景文化、知识。本平台想要利用这些不同形式的信息，为阅读新闻进行扩充，使之能更好地从新闻资讯中获取、理解有效的信息。


## 版本
- npm 3.5.2
- nginx 1.12.2
- Python 3.6.5
- jieba 0.42.1
- Flask 1.0.2


## 项目介绍
- 对于新闻的分析，使用的是jieba分词和关键词抽取，分词的重要性是通过textrank排序；
- 通过Flask提供接口，和前端交互数据；
- 网页使用vue，页面上的布局和组件使用的是Element-UI组件；
- 相关知识（知识小卡片）的内容是使用复旦大学的CN-DBpedia知识图谱。


## 项目展示
![image](https://user-images.githubusercontent.com/52556187/109738785-6c616380-7c03-11eb-83af-24859f2b0a80.png)


[体验地址](http://101.133.175.218)
