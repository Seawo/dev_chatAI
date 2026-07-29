from fastapi import FastAPI
from pydantic import BaseModel

from chat.chat_manager import ChatManager

API_KEY = "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"

chat = ChatManager(API_KEY)

app = FastAPI()


class ChatRequest(BaseModel):
    player_id: str
    character_id: str
    world_id: str 
    message: str


@app.post("/chat")
def chat_api(request: ChatRequest):

    result = chat.chat(
        request.player_id,
        request.character_id,
        request.world_id,
        request.message
    )

    return {
        "success": True,
        "answer": result["answer"],
        "voice": result["voice"]
    }