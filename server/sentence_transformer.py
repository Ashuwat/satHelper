from helperFunc.pre_processing import parquet_to_tabular
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def sentence_transformer():
    stored_queries = parquet_to_tabular('./dataset/tabular.parquet')

    model = SentenceTransformer('all-MiniLM-L6-v2')

    query_vectors = model.encode(stored_queries, normalize_embeddings=True) 

    query_vectors = np.array(query_vectors).astype('float32') #this should be default

    index = faiss.IndexFlatIP(query_vectors.shape[1])  # cosing similarity
    index.add(query_vectors)

    # Encode the new query and normalize
    new_query = """
    A pizzeria charges $17 for Pizza A and $13 for Pizza B. Ingredient costs are $450 per week for Pizza A and $310 per week for Pizza B. Last week, the pizzeria sold an equal number of both pizza types, and the weekly profit from the sale of each pizza type was the same. If x represents the number of Pizza B sold, what is the value of x?"""
    new_query_vector = model.encode([new_query], normalize_embeddings=True).astype('float32') #this should be on default
    distances, indices = index.search(new_query_vector, k=5)
    best_match_idx = indices[0][0]
    best_match_score = distances[0][0]

    return f"Best match: {stored_queries[best_match_idx]} (Similarity: {best_match_score:.4f})"

sentence_transformer()
