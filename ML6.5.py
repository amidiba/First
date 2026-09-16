from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, _= make_blobs(n_samples=500, centers=3, cluster_std=0.7, random_state=0)

# پیدا کردن K بهینه
inertia_list = []
for i in range(1, 15):
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(X)
    inertia_list.append(km.inertia_)

plt.plot(range(1, 15), inertia_list, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.show()