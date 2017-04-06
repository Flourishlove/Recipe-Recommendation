# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.spatial.distance
import pickle 

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

n_clusters = 2
labels = ('lab 1', 'lab 2')

X = list()

X.append([False,False,False,False,False])
X.append([False,True,False,False,False])
X.append([False,True,False,True,False])
X.append([False,False,False,True,True])
X.append([False,False,True,True,True])

X = np.array(X)

model = AgglomerativeClustering(n_clusters=n_clusters, linkage="average", affinity="hamming")

model.fit(X)
print model.labels_

"""
with open('yummly_clean.pkl', 'rb') as f:
    data = pickle.load(f)
print data
"""
