# Use Gemini to make a phrase your question in the right way 
# Use a KNN to vectorize the data and use it to get the most relevant problems
from helperFunc.pre_processing import parquet_to_tabular

if __name__ == "__main__":
    x = parquet_to_tabular('./dataset/tabular.parquet')
    
