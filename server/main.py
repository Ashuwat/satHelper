# Use Gemini to make a phrase your question in the right way 
# Use a KNN to vectorize the data and use it to get the most relevant problems
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from sentenceTransformer import sentenceTransformer
from gemini_route import preProcessing_gemini
app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace "*" with allowed origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

class Data(BaseModel):
    message: str
    value: bool

#post
index = 0
@app.post("/data")
async def post_data(data: Data):
    print(f"Received data: {data}")
    if (data.value == False):
        index = 0
        method = preProcessing_gemini(data.message)
        query, answer = sentenceTransformer(data.message, index)
    elif (data.value == True):
        index += 1
        method = preProcessing_gemini(data.message)
        query, answer = sentenceTransformer(data.message, index)
    return JSONResponse(content={"query": query, "method": method, "answer": answer})

# #get
# @app.get("/data")
# async def get_data():
#     data = {"name": "John", "age": 30}
#     return data
