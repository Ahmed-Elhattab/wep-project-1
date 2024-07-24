from fastapi import FastAPI
myapp = FastAPI()

@myapp.get('/')
def index():
    return {'data': 'name':'ahmed'}


@myapp.get('/about')
def about():
    return {'data': {'about page'}}






