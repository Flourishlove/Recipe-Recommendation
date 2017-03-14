#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:49:56 2017

@author: yujia
"""

import cPickle as pickle  
f = open('yummly.pkl')  
info = pickle.load(f)  
print (info)   #show file  