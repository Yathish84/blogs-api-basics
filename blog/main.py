from fastapi import FastAPI
from blog.schemas.schemas import Blog

app = FastAPI()

@app.get("/blog")
def all_blogs():
    return "all blogs"

@app.post("/blog")
def create_blog(request:Blog):
    return "creating"