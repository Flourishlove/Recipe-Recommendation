import csv
import numpy as np


with open('Recipe_clean_final.csv', 'rb') as f:
    reader = csv.reader(f)
    recipes = list(reader)
    # print recipes
with open('ingr_info.csv', 'rb') as f:
    reader = csv.reader(f)
    ingres = list(reader)

recordContain = []
for recipeLine in recipes:
    recipeIndex = recipeLine[0]
    recipeName = recipeLine[1]
    ingreList = recipeLine[2:] #list of ingredients for one recipe
    ingreNum = len(ingreList)
    flag = 0
    for _ingre in ingreList: #each ingredient for one recipe
        # new_list = []
        # flag = 0
        _ingreWord = _ingre.split(' ')
        _flag = 0
        for _eachIngreWord in _ingreWord:
            __flag = 0
            for ingreLine in ingres:
                ingreIndex = ingreLine[0]
                ingre = ingreLine[1]
                ingre = ingre.replace("_", " ")
                ingreLine[1] = ingre
                if _eachIngreWord in ingre:
                    _flag = 1
                    # print _eachIngreWord, ingre
                    break
            if __flag == 1:
                _flag = 1
                break
        if _flag == 1:
            flag = flag + 1
    if flag > 0:
        newList = []
        newList.append([recipeIndex, recipeName, ingreLine])
        recordContain.append(newList)
        print newList
# print recordContain
with open("cleanedRecipe.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(recordContain)
# print cleanedData



