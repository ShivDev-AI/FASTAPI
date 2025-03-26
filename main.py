from fastapi import FastAPI, HTTPException, Depends, Form, Body
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status

app = FastAPI()

# Dummy database
users_db = {}
products_db = {
    1: {"name": "Laptop", "price": 1000.0, "description": "A high-performance laptop"},
    2: {"name": "Smartphone", "price": 500.0, "description": "Latest model smartphone"},
}

# Models
class Product(BaseModel):
    name: str
    price: float
    description: str

class User(BaseModel):
    username: str
    password: str

# OAuth2 password bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake user authentication (in-memory)
def fake_user_auth(username: str, password: str):
    if users_db.get(username) and users_db[username]["password"] == password:
        return {"username": username}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = {"password": user.password}
    return {"msg": "User registered successfully"}

@app.post("/token")
async def login_for_access_token(form_data: User):
    user = fake_user_auth(form_data.username, form_data.password)
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/products", response_model=List[Product])
async def get_products():
    return list(products_db.values())

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def add_product(product: Product):
    product_id = len(products_db) + 1
    products_db[product_id] = product.dict()
    return products_db[product_id]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[product_id] = product.dict()
    return products_db[product_id]

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[product_id]
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)