from fastapi import APIRouter

router = APIRouter()

@router.post("/decide-tiebreaker")
async def decide_tiebreaker(data: dict):
    captions = data.get("captions", [])
    if not captions:
        return {"error": "No captions provided"}
    
    best_caption = captions[0]  # Placeholder AI logic (Replace with real AI)
    
    return {"best_caption": best_caption}
