import csv
import numpy as np

with open('ingre_comp.csv', 'rb') as f:
    reader= csv.reader(f)
    pairs = list(reader)
len = len(pairs)
i = 0
indexList = []
while i < len:
    ingre = pairs[i][0]
    comp = pairs[i][1]
    j = i + 1
    newList = []
    newList.append(ingre)
    newList.append(comp)
    while j < len and pairs[j][0]==ingre:
        newList.append(pairs[j][1])
        j = j + 1
    indexList.append(newList)
    i = j
print indexList
with open("newIngreComp.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(indexList)