from fastapi import FastAPI,HTTPException
from app.schemas import WordResponse
from app.routers import words,practice
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from sqlalchemy.orm import Session
from app.database import get_db

Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

app.include_router(
    words.router,
    prefix='/api',
    tags=["words"]
)

# @app.get("/api/word", response_model=WordResponse)
# def get_random_word():
#     """Get a random word"""
#     # TODO Write logic here....
#     # return WordResponse(
#     #     id= 12,
#     #     word= "book",  
#     #     definition= "Reading material for sleep",
#     #     difficulty_level= "Beginner"
#     # )

#     words = []
#     if len(words) == 0:
#         raise HTTPException(
#             status_code =404,
#             detail='No words available in database'
#         )

@app.get("/")
def read_root():
    return {
        "message": "Vocabulary Practice API",
        "version": "1.0.0",
        "endpoints": {
            "random_word": "/api/word",
            "validate": "/api/validate-sentence",
            "summary": "/api/summary",
            "history": "/api/history"
        }
    }