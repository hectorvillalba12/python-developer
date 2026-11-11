
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid
app = FastAPI()

#lista
posts = []

#post model
class Post(BaseModel):
    id: Optional [str]
    title: str
    autor: str
    content: Text
    create_at: datetime = datetime.now()
    publishet_at: Optional [datetime]
    publishet: bool = False

#peticion get (obtener)
@app.get("/")
def read_root():
    return {"welcome": "bienvenido"}

@app.get('/posts') #obtener publicaciones
def get_posts():
    return posts

#peticion post (crear)
@app.post('/posts')
def save_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    
    print(post_id)
    return "recived"