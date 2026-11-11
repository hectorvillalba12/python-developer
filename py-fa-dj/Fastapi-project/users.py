from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#entidad user
class User(BaseModel): #basemodel nos da la capacidad de crear una entidad
    name: str
    surname:str
    url:str
    age:int

users_list =[User(name ="hector", surname = "villalba", url = "https://hector.dev", age = 21),
            User(name ="roberto", surname = "gomez", url = "https://robert.dev", age = 30),
            User(name ="juan", surname = "basilio", url = "https://juan.dev", age = 40)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "hector", "surname": "villalba", "url": "https://hector.dev","age": 21},
            {"name": "roberto", "surname": "gomez", "url": "https://robert.dev", "age": 30},
            {"name": "juan", "surname": "basilio", "url": "https://juan.dev", "age": 40}]

@app.get("/users")
async def users():
    return users_list