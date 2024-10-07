import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv('kmdat.csv')
X = data.values

# Define the number of clusters
k = 3

# Initialize centroids randomly from the data points
np.random.seed(42)
initial_centroids_indices = np.random.choice(X.shape[0], k, replace=False)
centroids = X[initial_centroids_indices]

# Function to compute the distance between points and centroids
def compute_distances(points, centroids):
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
    return distances

# K-Means clustering algorithm
def kmeans(X, k, max_iters=100):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    for _ in range(max_iters):
        distances = compute_distances(X, centroids)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, labels

# Run K-Means
centroids, labels = kmeans(X, k)

# Organize points into clusters
clusters = [[] for _ in range(k)]
for label, point in zip(labels, X):
    clusters[label].append(point)

# Display the clusters
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}:",end= ' ')
    for point in cluster:
        print(point, end= ' ')
    print()