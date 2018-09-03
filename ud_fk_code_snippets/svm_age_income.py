# Create fake income/age clusters for N people in k clusters
import numpy as np
import matplotlib.pyplot as plt


def create_clustered_data(N, k):
    points_per_cluster = float(N)/k
    X = []
    y = []
    for i in range(k):
        income_centroid = np.random.uniform(20000.0, 200000.0)
        age_centroid = np.random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 100000.0), np.random.normal(age_centroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y


(X, y) = create_clustered_data(100, 5)
plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=y.astype(np.float))
# plt.show()

# Use SVC to partition graph into clusters
from sklearn import svm, datasets

C = 1.0
support_vector_classification = svm.SVC(kernel='linear', C=C).fit(X, y)


# By setting up a dense mesh of points in the grid and classifying all of them, we can render
# the regions of each cluster with different colors
def plot_predictions(clf):
    xx, yy = np.meshgrid(np.arange(0, 250000, 10), np.arange(10, 70, 0.5))
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    plt.figure(figsize=(8, 6))
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y.astype(np.float))
    plt.show()


# plot_predictions(support_vector_classification)

support_vector_classification.predict([200000, 40])

support_vector_classification.predict([50000, 65])
