import pandas as pd
import numpy as np 
from collections import Counter

def parquet_to_tabular(input):
    data = pd.read_parquet(input)
    query_list = data["query"].apply(lambda q: q.split("Answer Choices:")[0].strip()).tolist()
    # answer_list = data["gold"].apply(lambda a: str(a[0]) if isinstance(a, list) else str(a)).tolist()
    # choices_list = data["choices"].apply(lambda c: [x.strip() for x in c[0].split(",")]).tolist()
    return query_list

def euclidean_distance(point1, point2): 
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))
