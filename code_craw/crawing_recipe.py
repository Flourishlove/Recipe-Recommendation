#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:44:25 2017

@author: yujia
"""

import urllib
from scrapy import Selector

def getHtml(url1):
    with urllib.request.urlopen(url1) as url:
        html = url.read()
    return html
    

def parse(url,response):
        selector = Selector(response)
        # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
        # 这个list里的每一个元素都是我们要找的html标签
        content_list = selector.xpath("//*[@class='topic']")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处解析标签，提取出我们需要的帖子标题。
            topic = content.xpath('string(.)').extract_first()
            print (topic)
            # 此处提取出帖子的url地址。
            url = url.host + content.xpath('@href').extract_first()
            print (url)

url="http://www.yummly.co/#recipe/The-Best-Effing-Chicken-Recipe-Ever_-Seriously_-1697567"
html = getHtml(url)

parse(url,html)

#print (html)