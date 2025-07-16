import os 
import sqlmodel 
from sqlmodel import Session,SQLModel

DATABASE_URL=os.environ.get("DATABASE_URL")

if DATABASE_URL == "" :
    raise NotImplementedError("`Database_URL` needs to be set ")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
     print("creating Database Tables..")
     SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
    
    