# import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial.distance
# import pickle 

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

n_clusters = 2
labels = ('lab 1', 'lab 2')

X = list()

X.append([0,0,0,0,0])
X.append([0,1,0,0,0])
X.append([0,1,0,1,0])
X.append([0,0,0,1,1])
X.append([0,0,1,1,1])

X = np.array(X)

model = AgglomerativeClustering(n_clusters=n_clusters, linkage="average", affinity="hamming")

model.fit(X)
print model.labels_

"""
with open('yummly_clean.pkl', 'rb') as f:
    data = pickle.load(f)
print data
"""
