from fastapi import FastAPI
from indb import generate_products
from product import Product


app = FastAPI()

products = generate_products()

@app.get('/products')
def get_products():
    return {"Products" : products}


@app.post('/products')
def create_product(product: Product):
    return {"products": product}