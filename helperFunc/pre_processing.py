import pandas as pd
import numpy as np 
from collections import Counter

def parquet_to_tabular(input):
    data = pd.read_parquet(input)
    x = (data.iloc[0]["query"])
    x = x.split("Answer Choices:")[0].strip()
    print(x)


def euclidean_distance(point1, point2): 
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

class KNN_Classifier():
    def __init__(self, k = 1, distance = 'path'):
        self.k = k
        self.distance = distance
    
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        print(x_test)

    def knn_predict(training_data, training_labels, test_point, k):
        distances = []
        for i in range(len(training_data)):
            dist = euclidean_distance(test_point, training_data[i])
            distances.append((dist, training_labels[i]))
        distances.sort(key=lambda x: x[0])
        k_nearest_labels = [label for _, label in distances[:k]]
        return Counter(k_nearest_labels).most_common(1)[0][0]
    