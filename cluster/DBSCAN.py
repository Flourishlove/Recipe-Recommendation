import csv
import numpy as np
import pandas as pd
import scipy.spatial.distance

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

with open('training_data.csv', 'rb') as f:
    reader = csv.reader(f)
    train = list(reader)

train = np.array(train)

model = DBSCAN(eps=0.08, min_samples=50, metric="hamming").fit(train)

print model.labels_

df = pd.DataFrame(model.labels_)
df.to_csv("some.csv")
