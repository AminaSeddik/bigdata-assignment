import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("res_dpre.csv")
features = df[['Age', 'Fare']].dropna()
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(features)
df['Cluster'] = kmeans.labels_

df['Cluster'].value_counts().to_csv("k.txt", header=False)
print("K-Means clustering done, results saved in k.txt")