from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # This is how we implememt query parameters
    # http://127.0.0.1:8000/blog?limit=1&published=False
    if published:
        return {'data': f'blog list has {limit} blogs'}
    else:
        return {'data': f'blog list has no blogs'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

