from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class Data(BaseModel):
    message: str
    value: str

@app.get("/data", response_model=Data)
def get_data():
    data = {"message": "yo", "value": "some value"}
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
