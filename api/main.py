from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# for firebase auth
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response

from enum import Enum
from typing import Union
from pydantic import BaseModel
import os

from firebase_admin import auth, credentials
import firebase_admin

# initialize firebase admin
cred = credentials.Certificate("./api/firebase_credentials.json")
firebase_admin.initialize_app(cred)


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
    "*",
    # "application/json",
    # "X-AUTH-TOKEN"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=allowed_methods,
    allow_headers=allowed_headers
)


def get_user(res: Response,
             cred: HTTPAuthorizationCredentials=Depends(HTTPBearer(auto_error=False))):
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )
    res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
    return decoded_token

# root
@app.get("/")
async def root():
    return {"message": "This is the root."}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


@app.get("/user")
async def user(user_info=Depends(get_user)):
    return {"message": "User",
            "user_info": user_info}
