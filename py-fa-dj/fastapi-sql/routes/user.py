from fastapi import APIRouter #apiroutes nos permite definir las rutas por separado
from config.db import conn
from models.user import users

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users")
def creat():
    return "hola mundo"



@user.get("/users")
def holamundo():
    return "hola mundo"



@user.get("/users")
def holamundo():
    return "hola mundo"



@user.get("/users")
def holamundo():
    return "hola mundo"