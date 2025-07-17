from fastapi import FastAPI
from api.db import init_db
from api.chat.routing import router as chat_router
from sqlmodel import SQLModel
from api.db import engine 

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix='/api/chats')

@app.get("/")
def read_index():
    return {"hello":"world Again XXXX"}

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)