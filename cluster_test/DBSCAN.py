import numpy as np
import scipy.spatial.distance

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

X = list()

X.append([0,0,0,0,0])
X.append([0,1,0,0,0])
X.append([0,1,0,1,0])
X.append([0,0,0,1,1])
X.append([0,0,1,1,1])

X = np.array(X)

model = DBSCAN(eps=0.3, min_samples=3, metric="hamming").fit(X)

print model.labels_
