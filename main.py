from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data': {
        'name': 'Shubham'
    }}


@app.get('/about')
def about():
    return {'data': 'First About Page'}