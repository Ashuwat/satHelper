# Use Gemini to make a phrase your question in the right way 
# Use a KNN to vectorize the data and use it to get the most relevant problems
from pre_processing import parquet_to_tabular
from cors_config import add_cors_middleware
from fastapi import FastAPI

app = FastAPI()

add_cors_middleware(app)

@app.get("/data")
async def get_data():
    return {'message': 'message recieved in backend'}
