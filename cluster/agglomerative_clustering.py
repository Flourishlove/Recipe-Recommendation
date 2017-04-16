# import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import scipy.spatial.distance
import pickle

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

n_clusters = 8
labels = ['lab 1', 'lab 2', 'lab 3', 'lab 4', 'lab 5', 'lab 6', 'lab 7', 'lab 8']

with open('training_data.csv', 'rb') as f:
    reader = csv.reader(f)
    train = list(reader)

train = np.array(train)

model = AgglomerativeClustering(n_clusters=n_clusters, linkage="average", affinity="hamming")

model.fit(train)
print model.labels_

df = pd.DataFrame(model.labels_)
df.to_csv("some.csv")

"""
with open('some.csv', 'wb') as fw:
    writer = csv.writer(fw)
    writer.writerows(X)
"""
