from typing import Optional, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "fav food", "content": "I like pizza", "id": 2},
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_Posts():
    return {"data": my_posts}


@app.post("/posts")
def posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
