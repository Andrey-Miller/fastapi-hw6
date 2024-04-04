from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from store import database
import users
import products
import orders
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Добро пожаловать в интернет-магазин!</h1>"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)