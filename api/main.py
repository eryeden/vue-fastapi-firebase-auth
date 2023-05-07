from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from typing import Union
from pydantic import BaseModel
import os


app = FastAPI()

# Configurations for CORS:
# The following means;
allowed_origins = [
    "http://localhost:5173"
]

allowed_methods = [
    "POST",
    "GET"
]

allowed_headers = [
    # "*",
    "application/json"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=allowed_methods,
    allow_headers=allowed_headers
)


# root
@app.get("/")
async def root():
    return {"message": "This is the root."}


@app.get("/hello")
async def root():
    return {"message": "Hello World"}
