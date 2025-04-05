from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return "Hello User!"

@app.get("/property/{id}")
def property(id : int):
    return {f"property_id: {id}"}

@app.get("/profile/{username}")
def profile(username: str):
    return {f"Hi {username} , Welcome to the profile page!"}

@app.get("/movies/")
def get_movies():
    return {"movies": ["Inception", "Interstellar", "Dunkirk"]}