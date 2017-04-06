import csv


with open('Recipe_clean_final.csv', 'rb') as f:
    reader = csv.reader(f)
    recipes = list(reader)
    # print recipes
with open('ingr_info.csv', 'rb') as f:
    reader = csv.reader(f)
    ingres = list(reader)
# print ingredients

cleanedData = []

for recipeLine in recipes:
    recipeIndex = recipeLine[0]
    recipeName = recipeLine[1]
    ingreList = recipeLine[2:] #list of ingredients for one recipe
    for ingreLine in ingres:
        ingreIndex = ingreLine[0]
        ingre = ingreLine[1]
        ingre = ingre.replace("_", " ")
        ingreLine[1] = ingre
        # print ingre
    newIngreList = []
    for ingre in ingreList:
        # print ingre
        if ingre != '':
            newIngreList.append(ingre)
    cleanedData.append(newIngreList)

# with open("Recipe_clean_final.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(cleanedData)
# # print cleanedData



