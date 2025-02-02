from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from agent import run_agent

app = FastAPI()

class Data(BaseModel):
    message: str
    value: str

def post(query): #use when doing app@get
    print('this is supposed to be retrieving stuff')
    if isinstance(query, str):
        run_agent(query)
        return 0
    if (query == True):
        print('this is what is supposed to happen when the action is nothing')
        return 0
    elif(query == False):
        print('')
        return 0

# def get(): #use when posting
#     print('this is supposed to be doing posting stuff')
