from numpy import random, array


# Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    points_per_cluster = N/k
    X = []
    for i in range(k):
        income_centroid = random.uniform(20000.0, 200000.0)
        age_centroid = random.uniform(20.0, 70.0)

        for j in range(int(points_per_cluster)):
            X.append([random.normal(income_centroid, 10000.0), random.normal(age_centroid, 2.0)])

    X = array(X)
    return X


# use k-means to rediscover these clusters in unsupervised learning

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

data = createClusteredData(100, 6)

model = KMeans(n_clusters=6)

# scale the data to normalize it
model = model.fit(scale(data))

# model = model.fit(data)

print(model.labels_)

# Visualize

plt.figure(figsize=(8,6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()
