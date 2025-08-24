from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def vamshi():
    return 'Hello VAMSHI'

@app.get('/about')
def about():
    return {'about':'we are in about page'}