from helperFunc.pre_processing import parquet_to_tabular
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np

def sentence_transformer():
    stored_queries = parquet_to_tabular('./dataset/tabular.parquet')

    vectorizer = TfidfVectorizer()
    query_vectors = vectorizer.fit_transform(stored_queries)

    # Fit k-NN (cosine similarity)
    knn = NearestNeighbors(n_neighbors=5, metric='cosine')
    knn.fit(query_vectors)

    # New query
    new_query = """
    A pizzeria charges $17 for Pizza A and $13 for Pizza B. Ingredient costs are $450 per week for Pizza A and $310 per week for Pizza B. Last week, the pizzeria sold an equal number of both pizza types, and the weekly profit from the sale of each pizza type was the same. If x represents the number of Pizza B sold, what is the value of x?"""
    new_query_vector = vectorizer.transform([new_query])

    # Find similar queries
    distances, indices = knn.kneighbors(new_query_vector)

    # Print results
    best_sim_score = [0, 0]
    for idx, (dist, i) in enumerate(zip(distances[0], indices[0])):
        if (1 - dist > best_sim_score[0]):
            best_sim_score = [1 - dist, i]

    return (f"{stored_queries[best_sim_score[1]]}")

x = sentence_transformer()

print(x)
