import csv
import numpy as np
import time


with open('cleanedRecipe.csv', 'rb') as f:
    reader = csv.reader(f)
    recipes = list(reader)
    # print recipes
with open('ingr_info.csv', 'rb') as f:
    reader = csv.reader(f)
    ingres = list(reader)
with open('newIngreComp.csv', 'rb') as f:
    reader= csv.reader(f)
    pairs = list(reader)
    # print pairs

t = time.time()

recipeComp=[[0]*1111 for i in range(15874)]
j = -1
for recipeLine in recipes:
    print j
    # print recipeLine
    j = j + 1
    recipeComp[j][0] = recipeLine[0]
    recipeComp[j][1] = recipeLine[1]
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
                    for row in pairs:
                        if row[0] == ingreIndex:
                            for _index in row[1:]:
                                recipeComp[j][int(_index)+2] = 1
                                # print recipeComp[j][0:2]
                    ## search for compound and add compound to list
with open("recipeCompound.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(recipeComp)
# print cleanedData

print time.time() - t

