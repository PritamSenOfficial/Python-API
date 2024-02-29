# This is the code for creat an API using Python Fast API
from typing import Union
from fastapi import FastAPI, Response, HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange
app = FastAPI()

class post(BaseModel):
    Title: str
    Body:str
    # Publish: bool = True

my_data = [{"title":"1st", "Body":"1st", "id":1},{"title":"2st", "Body":"2st", "id":2},{"title":"3st", "Body":"3st", "id":3}]

@app.get("/")   
def read_root():
    return {"Hello": my_data}

@app.post("/post",status_code=status.HTTP_201_CREATED)   
def read_test(Npost: post):
    # print(Npost)
    x = Npost.dict()
    x['id'] = randrange(4,100000000)
    my_data.append(x)
    return {"Hi ": x}

def find_post(id):
    for i  in my_data:
        if i['id'] == id:
            return i

@app.get("/post/letest")
def get_letest_post():
    post = my_data[-1]
    return {"Here":post}

@app.get("/items/{id}")
def read_item(id:int, respond : Response):
    post = find_post(int(id))
    if not post:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"Massge":f"post of {id} not found"}))
        # return {"Massge":f"post of {id} not found"}
    return {"item_id_ok_test": post} 