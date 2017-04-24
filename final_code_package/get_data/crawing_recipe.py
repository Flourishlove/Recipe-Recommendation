#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:44:25 2017

@author: yujia
"""

import urllib
import re
import pandas as pd

def getHtml(url1):
    with urllib.request.urlopen(url1) as url:
        html = url.read().decode("utf-8")
    return html
   

#yum=yum[yum.cuisine == 'Chinese']
def crawling_image(yum):
    result=[]
    i=0
    for rec in yum['id']:
        i=i+1
        url="http://www.yummly.co/#recipe/"+str(rec)
        html = getHtml(url)
    
        imgs=re.findall('\"name\"\: \"(.*?)\",\n *?\"image\": \"(.*?)\",\n *?\"description\": \"(.*?)\"',html)
        result.extend(imgs)
              
    #nutrition=re.findall('\"nutrition\"\: {\(\n *?|.*\)*}',html)
        print(i,len(imgs))
    
    distinct=list(set(result))
    i=0
    recipe=[]
    for k in range(len(yum)):
        for name in distinct:
            if yum['recipeName'][k]==name[0]:
                recipe.append((yum['id'][k],yum['recipeName'][k],name))
    return recipe