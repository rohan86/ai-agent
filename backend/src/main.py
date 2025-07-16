from fastapi import FastAPI
from backend.src.api.db import init_db

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db
    yield

app = FastAPI()

@app.get("/")
def read_index():
    return {"hello":"world Again"}