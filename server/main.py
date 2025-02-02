# Use Gemini to make a phrase your question in the right way 
# Use a KNN to vectorize the data and use it to get the most relevant problems
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class Data(BaseModel):
    message: str
    value: str

#post
@app.post("/data")
async def post_data(data: Data):
    print(f"Received data: {data}")
    
    return JSONResponse(content={"message": "Data received successfully", "received_data": data.dict()})

# #get
# @app.get("/data")
# async def get_data():
#     data = {"name": "John", "age": 30}
#     return data
