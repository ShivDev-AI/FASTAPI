from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello, World!"

@app.get("/next")
def index():
    return "Again Hello, World!"