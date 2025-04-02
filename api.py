from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

static_string = "Hello World!"

def returnMessage(text: str | None = None):
    return {"message": text or static_string}

@app.get("/get-message")
async def read_root():
    return returnMessage()

@app.get("/hello")
async def hello(name):
    return returnMessage("Hello "+name+"!")

@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return returnMessage()

@app.put("/change")
async def update_text(text: str):
    global static_string
    static_string += text
    return returnMessage()

@app.delete("/reset")
async def reset():
    global static_string 
    static_string = "Hello World!"
    return returnMessage()