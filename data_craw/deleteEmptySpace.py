import csv


with open('Recipe_clean_demo.csv', 'rb') as f:
    reader = csv.reader(f)
    recipes = list(reader)

cleanedData = []

for recipeLine in recipes:
    recipeIndex = recipeLine[0]
    recipeName = recipeLine[1]
    ingreList = recipeLine[2:] #list of ingredients for one recipe
    newIngreList = []
    for ingre in ingreList:
        # print ingre
        if ingre != '':
            newIngreList.append(ingre)
    cleanedData.append(newIngreList)

with open("Recipe_clean_final.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(cleanedData)
# print cleanedData



