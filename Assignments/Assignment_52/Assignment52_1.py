import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

datset_path = "student-mat.csv"

df = pd.read_csv(datset_path)

print("Few records from dataset : \n")
print(df.head())
print("Shape of dataset : ", df.shape)

columns = ["studytime", "failures", "absences","G1","G2","G3"]

X = df[columns]

kmeans = KMeans(n_clusters=3, random_state=0)

kmeans.fit(X)

Ymeans = kmeans.predict(X)
centers = kmeans.cluster_centers_

clusters = []
performance = []

# cluster_dict = {
#     0 : 'Struggling',
#     1 : 'Average',
#     2 : 'Top'
# }

for y in Ymeans:
    clusters.append(y)
    # performance.append(cluster_dict[y])

X['Clusters'] = clusters
# X['Performance'] = performance

X.to_csv('Student_Performance.csv') 

plt.figure(figsize=(8,6))
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroids')

plt.title('K-means Clustering Example')

plt.legend()
plt.show()

