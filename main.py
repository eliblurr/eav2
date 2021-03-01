from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from static.main import image_DIR
from fastapi import FastAPI

origins = ["http://localhost/*", "https://localhost/*", "*"]

api = FastAPI(docs_url="/docs")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authenticate")
api.mount('/images', StaticFiles(directory=f"{image_DIR}"), name='images')
api.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

from views import *