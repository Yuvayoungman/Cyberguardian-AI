from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini import analyze_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CyberGuardian backend is running"}

@app.post("/analyze")
def analyze(data: dict):
    try:
        text = data.get("text")
        if not text:
            return {"error": "No text provided"}

        result = analyze_text(text)
        return {"result": result}

    except Exception as e:
        # 🔴 THIS IS IMPORTANT
        print("🔥 GEMINI ERROR:", str(e))
        return {"error": str(e)}
