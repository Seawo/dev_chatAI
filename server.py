from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from chat.chat_manager import ChatManager

API_KEY = "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"

chat = ChatManager(API_KEY)

app = FastAPI()

app.mount(
    "/voices",
    StaticFiles(directory="data/voices"),
    name="voices"
)


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