from pre_processing import parquet_to_tabular
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def sentenceTransformer(query):
    stored_queries = parquet_to_tabular('./dataset/tabular.parquet')

    model = SentenceTransformer('all-MiniLM-L6-v2')

    query_vectors = model.encode(stored_queries, normalize_embeddings=True) 

    query_vectors = np.array(query_vectors).astype('float32') #this should be default

    index = faiss.IndexFlatIP(query_vectors.shape[1])  # cosing similarity
    index.add(query_vectors)

    # Encode the new query and normalize
    new_query = query #get input
    new_query_vector = model.encode([new_query], normalize_embeddings=True).astype('float32') #this should be on default
    distances, indices = index.search(new_query_vector, k=5)
    best_match_idx = indices[0][0]
    best_match_score = distances[0][0]

    return f"{stored_queries[best_match_idx]}"
