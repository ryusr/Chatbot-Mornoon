from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.model import ask_llama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    image_base64 = data.get("image", None)

   
    if image_base64:
        print("Received image.")

    reply = ask_llama(user_message)
    return {"response": reply}

