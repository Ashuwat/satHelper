import pandas as pd
import numpy as np 
from collections import Counter

def parquet_to_tabular(input):
    data = pd.read_parquet(input)
    query_list = data["query"].apply(lambda q: q.split("Answer Choices:")[0].strip()).tolist()
    return query_list

def euclidean_distance(point1, point2): 
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

parquet_to_tabular('./dataset/tabular.parquet')
