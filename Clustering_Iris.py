import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Membaca dataset Iris
iris = pd.read_excel('C:/Users/david/Documents/my private document/tugas kuliah/Semester 5/Workshop Sistem Cerdas/archive/iris_dataset.xlsx', sheet_name=0, header=3, usecols='D:H')

# Menyusun target latih
target = iris.iloc[:, 4].values
target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
target = [target_mapping[label] for label in target]

# Menyusun variabel x dan y
X = iris.iloc[:, 2:4].values

# Klasifikasi menggunakan kmeans
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Memprediksi label klaster
predicted_labels = kmeans.labels_

# Menghitung akurasi
accuracy = accuracy_score(target, predicted_labels)
print("Accuracy:", accuracy)

# Menampilkan plot hasil klastering
plt.figure()
plt.scatter(X[predicted_labels == 0, 0], X[predicted_labels == 0, 1], s=60, c='white', label='Setosa', marker='o', edgecolors='red', linewidths=2)
plt.scatter(X[predicted_labels == 1, 0], X[predicted_labels == 1, 1], s=60, c='white', label='Versicolor', marker='o', edgecolors='lime', linewidths=2)
plt.scatter(X[predicted_labels == 2, 0], X[predicted_labels == 2, 1], s=60, c='white', label='Virginica', marker='o', edgecolors='blue', linewidths=2)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=80, c='black', marker='x', label='Centroids', linewidths=2)
plt.title('Clustering Iris Data Set dengan Kmeans')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
plt.grid(True)
plt.show()

