from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/echo")
def echo(message: str):
    return {"message": message}


@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour"}
