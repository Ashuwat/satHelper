from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class Data(BaseModel):
    message: str
    value: int

@app.post("/data")
async def receive_data(data: Data):
    print(f"Received data: {data}")
    return JSONResponse(content={"status": "success", "received": data.dict()})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
