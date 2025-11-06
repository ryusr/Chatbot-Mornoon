## Kitty Chat (Thai Health Assistant)

An ultra-light chat UI with a FastAPI backend that calls a hosted LLM to role-play a friendly Thai health advisor named "หมอนุ่น". Includes background music, sound effects, and selectable background themes with matching color palettes.

### Features
- Chat interface with user/bot message bubbles and avatar
- Background music (play/pause) and SFX volume controls
- Four background themes with matching UI palettes:
  - bg1: Green (default)
  - bg2: Minty Blue
  - bg3: Sunny Yellow
  - bg4: Sleepy Purple
- Theme persists via localStorage; selection is highlighted in settings
- FastAPI backend with CORS enabled

### Project Structure
- `frontend/`
  - `index.html` — Chat UI, settings modal, theme logic
  - `style.css` — Styles and theme variables
  - Media assets — `profile.jpg`, `bgmusic.mp3`, `pop1.mp3`, `pop2.mp3`, and `ิิbgall/bg*.jpg`
- `backend/`
  - `main.py` — FastAPI app exposing POST `/chat`
  - `model.py` — LLM call to Groq-compatible Chat Completions API

### Prerequisites
- Python 3.11+
- An API key for the LLM provider exposed at `https://api.groq.com/openai/v1/chat/completions`

### Setup
1) Install Python dependencies (PowerShell):
```powershell
pip install fastapi uvicorn[standard] python-dotenv requests
```

2) Create a `.env` file in the project root with your API key:
```env
LLM_API_KEY=your_api_key_here
```

### Run the Backend
From the project root:
```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```
This starts the FastAPI server at `http://127.0.0.1:8000`.

### Open the Frontend
Simply open `frontend/index.html` in your browser (double-click or drag into a tab). The page makes requests to `http://127.0.0.1:8000/chat`.

### API
POST `/chat`
```json
{
  "message": "text from user"
}
```
Response
```json
{
  "response": "text from bot"
}
```

### Theming
- Open Settings (ตั้งค่า) → Background section.
- Click a color block to set both the background image and the UI palette.
- The selected block is outlined; selection persists across reloads.

### Troubleshooting
- No bot response / errors in console:
  - Ensure the backend is running on port 8000.
  - Verify `.env` contains a valid `LLM_API_KEY` and restart the backend.
  - Check terminal logs for HTTP errors from the LLM API.
- CORS issues: Backend is configured to allow `*`. If you change hosts/ports, keep CORS in sync.
- Sound not auto-playing: Most browsers require a user interaction first; click anywhere to allow playback.

### Notes
- The backend currently sends a short system prompt defining the bot persona in Thai.
- Requests timeout after 60s with a friendly Thai error shown to users.

### License
For educational/demo use. Replace assets and prompts to suit your project.


