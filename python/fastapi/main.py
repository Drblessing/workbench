from fastapi import FastAPI
from enum import Enum
from fastapi.responses import FileResponse


class ModelName(str, Enum):
    llama = "llama"
    alpaca = "alpaca"
    pygmalion = "pygmalion"


app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return [
        1,
        2,
        3,
    ]


@app.options("/")
async def rootOption():
    return {"message": "What options do you have?"}


@app.get("/items/{item_id}")
async def read_item(item_id: float):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alpaca:
        return {"model_name": model_name, "message": "Alpacas are great!"}
    if model_name.value == "llama":
        return {"model_name": model_name, "message": "Llamas are cool!"}
    return {"model_name": model_name, "message": "Have some residuals"}


# Return ethereum pdf
@app.get("/ethereum.pdf")
async def ethereum_pdf():
    return FileResponse("ethereum.pdf")


# Return ethereum json
@app.get("/ethereum.json")
async def ethereum_json():
    return FileResponse("ethereum.json")


## Query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/query/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


## Request Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/post/items/")
async def create_item(item: Item):
    if item.tax:
        price_with_tax = item.price + item.tax
        return {**item.dict(), "price_with_tax": price_with_tax}
    return item


## Cookies
from fastapi import Cookie
from typing import Annotated
from fastapi.responses import HTMLResponse


@app.get("/cookies/")
async def read_cookies(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


@app.get("/set-cookies/")
async def set_cookies(name: str = "default", value: str = "default"):
    content = """
    <html>
        <body>
            <form action="/cookies/" method="get">
                <input type="text" name="ads_id" value="default">
                <input type="submit" value="Submit">
            </form>
            <div>
                <p>Set the cookies</p>
            </div>
        </body>
    </html>
    """
    response = HTMLResponse(content=content)
    response.set_cookie(key=name, value=value)
    return response


## Headers
from fastapi import Header


@app.get("/headers/")
async def read_headers(user_agent: Annotated[list[str] | None, Header()] = None):
    return {"User-Agent": user_agent}


## Form

from fastapi import Form


### Post form


### With built-in Form
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


### Testing simple body with Form
# @app.post("/login/")
# async def login(username: str, password: str):
#     return {"username": username}


### Form html
@app.get("/login/")
async def login_html():
    content = """
    <html>
        <body>
            <form action="/login/" method="post">
                <input type="text" name="username" value="default">
                <input type="password" name="password" value="default">
                <input type="submit" value="Submit">
            </form>
            <div>
                <p>Login</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=content)


## Files upload
from fastapi import File, UploadFile


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


### File upload html
@app.get("/uploadfile/")
async def upload_file_html():
    content = """
    <html>
        <body>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Submit">
            </form>
            <div>
                <p>Upload file</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=content)


## Static files
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
