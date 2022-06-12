from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel
from gen_api import start

from fastapi.middleware.cors import CORSMiddleware



class Item(BaseModel):
    projects: List[str] = [],
    values: List = []


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/items/")
def create_item(item: Item):
    return start(item.projects, item.values)