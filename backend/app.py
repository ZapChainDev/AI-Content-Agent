from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routes.content_routes import router as content_router
import ollama
import re
import os
import sys
import requests  # ✅ Add this at the top


# ✅ Ensure the "routes" directory is recognized
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ✅ Initialize FastAPI
app = FastAPI()

app.include_router(content_router, prefix="/api", tags=["content"])

# ✅ Enable CORS for Frontend Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# ✅ Define Request Model for AI Content Generation
class ContentRequest(BaseModel):
    topic: str
    content_type: str
    tone: str = "neutral"

# ✅ Home Route
@app.get("/")
def home():
    return {"message": "AI Content Generator API is running"}

# ✅ Generate Content API (Using `gemma:2b`)
@app.post("/generate")
def generate_content(request: ContentRequest):
    # ✅ Step 1: Adjust Prompt Based on Content Type
    if request.content_type == "caption":
        prompt = (
            f"Generate exactly 5 engaging social media captions about '{request.topic}' "
            f"in a {request.tone} tone. Each caption should be concise, formatted in **bold**, "
            f"and DO NOT include numbers. Separate each caption with a new line."
        )
    else:
        prompt = (
            f"Write a compelling {request.content_type} about '{request.topic}' in a {request.tone} tone. "
            f"Do NOT use bullet points or numbering, just write in paragraphs."
        )

    # ✅ Call Ollama Locally (Using `gemma:2b`)
    try:
        response = ollama.generate(model="gemma:2b", prompt=prompt)
        generated_text = response["response"]

        # ✅ Step 2: Remove AI-Generated Numbers for Captions Only
        if request.content_type == "caption":
            cleaned_captions = re.sub(r"^\s*\d+[\).]?\s*", "", generated_text, flags=re.MULTILINE)
            captions = [caption.strip() for caption in cleaned_captions.strip().split("\n") if caption.strip()]
            
            # ✅ Ensure Exactly 5 Captions
            while len(captions) < 5:
                captions.append("**(Generated placeholder caption to ensure 5 total items)**")

            formatted_output = "\n".join([f"{i+1}. {caption}" for i, caption in enumerate(captions[:5])])
        else:
            # ✅ Keep blog posts in normal paragraph format
            formatted_output = generated_text.strip()

        return {"generated_text": formatted_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama AI Error: {str(e)}")

# ✅ AI Tiebreaker Request Model
class TiebreakerRequest(BaseModel):
    captions: list[str]

# ✅ AI-Based Tiebreaker (Using `gemma:2b`)
@app.post("/decide-tiebreaker")
async def decide_tiebreaker(request: TiebreakerRequest):
    if not request.captions or len(request.captions) < 2:
        raise HTTPException(status_code=400, detail="At least two captions are required for tiebreaker.")

    try:
        # ✅ AI Prompt for Evaluating Captions
        prompt = f"""
        You are an expert in social media marketing. Choose the best caption from the list below that is most engaging, effective, and likely to perform well. Consider clarity, call-to-action, and emotional impact.

        Captions:
        {chr(10).join([f"{i+1}. {caption}" for i, caption in enumerate(request.captions)])}

        Respond with the best caption only.
        """

        # ✅ Call Ollama Locally (Using `gemma:2b`)
        response = ollama.chat(model="gemma:2b", messages=[{"role": "system", "content": prompt}])

        best_caption = response["message"]["content"].strip()

        print("🔍 AI Response:", best_caption)  # ✅ Log AI Output

        return {"best_caption": best_caption}

    except Exception as e:
        print("❌ AI Decision Error:", str(e))  # ✅ Log Error
        raise HTTPException(status_code=500, detail=str(e))
