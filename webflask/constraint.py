#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:14:50 2017

@author: yujia
"""


from nurtition import *
import numpy as np
import ast

def constraint_EER(my_nutrition, age, weight, height, gender, activity_level, standard):
    allow = 0.35
    #print(standard)
    #print(my_nutrition)
    #print('\n')
    if_satisfied = True
    n_nutrition= len(my_nutrition)
    for i in range(5):
#    for i in range(n_nutrition):
        if my_nutrition[i] < standard[i]*(1-allow) or my_nutrition[i] > standard[i]*(1+allow):
            if_satisfied = False

    return if_satisfied


def nutritional_constraints(yum, age, weight, height, gender, activity_level):
    yum_list=[]
    standard = nutrition(age, weight, height, gender, activity_level)
    standard = [standard[i]/2.7 for i in range(len(standard))]
    print standard
    nutrition_list=['ENERC_KJ', 'PROCNT', 'CHOCDF', 'FIBTG', 'FAT', 'CA', 'FE', 'MG', 'P', 'K',\
                    'NA', 'ZN', 'MN', 'SE', 'VITA_RAE', 'TOCPHA', 'VITC', 'RIBF', 'NIA', 'VITB6A', 'BITB12'
                    ,'CHOLN', 'VITK', 'FOL']
    unit_ratio=[1, 1, 1, 1, 1, 1000, 1000, 1000, 1000, 1000,\
                    1000, 1000, 1000, 1000000, 0.001, 1000, 1000, 1000, 1000, 1000, 1000000
                    ,1000, 1000000, 1000000]
    n_nutrition= len(nutrition_list)
    for recipe in yum:
        my_nutrition=[0 for i in range(n_nutrition)]
        temp_list = ast.literal_eval(recipe[1]) # convert unicode to python list of dictionary
        for element in temp_list:
            # print type(element)
            # print element
            for i in range(n_nutrition):
                if element['attribute'] == nutrition_list[i]:
                    my_nutrition[i] = element['value']*unit_ratio[i] #/recipe[14]

        yum_list.append([recipe[0], my_nutrition])
    N=len(yum_list)
    satisfied_list=[]
    for i in range(N):
        for j in range(i+1,N):
                for k in range(j+1, N):
                        my_nutrition = [x + y + z for x, y, z in zip(yum_list[i][1], yum_list[j][1], yum_list[k][1])]
                        if_satisfy = constraint_EER(my_nutrition, age, weight, height, gender, activity_level, standard)
                        if if_satisfy == True:
                            satisfied_list.append([yum_list[i][0], yum_list[j][0], yum_list[k][0]])
    #print(satisfied_list)
    print('Found Matches ', len(satisfied_list))
    return satisfied_list


#nutritional_constraints(yum1, 12, 65, 1.8, 'female', 'Active')