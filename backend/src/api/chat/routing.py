from fastapi import APIRouter ,Depends
from sqlmodel import Session
from api.db import get_session
from .models import ChatMessagePayload,ChatMessage   

router = APIRouter()


@router.get("/")
def chat_health():
    return{"status":"OK"}

# curl -X POST -d '{"message":"Hello World"}' -H "Content-Type: application/json" http://localhost:8080/api/chats
@router.post("/",response_model=ChatMessage)
def chat_create_message(payload : ChatMessagePayload, session: Session= Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
