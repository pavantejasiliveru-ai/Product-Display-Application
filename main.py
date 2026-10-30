from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from function import get_all_products, get_product_by_id
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def display_products(request: Request):
    products = get_all_products()
    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={"products": products}
    )

@app.get("/products/{product_id}")
def display_product(request: Request, product_id: int):
    product = get_product_by_id(product_id)
    return templates.TemplateResponse(
        request=request,
        name="product_detail.html",
        context={"product": product}

    )