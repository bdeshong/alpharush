from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

import models, schemas, database

router = APIRouter(prefix="/phrase", tags=["phrases"])

@router.get("/random", response_model=schemas.PhraseResponse)
def get_random_phrase(db: Session = Depends(database.get_db)):
    # Fetch a random phrase from the database
    random_phrase = db.query(models.Phrase).order_by(func.random()).limit(1).first()
    if random_phrase is None:
        raise HTTPException(status_code=404, detail="No phrases found")
    return random_phrase

# Optional: endpoint to get all phrases (for testing/debugging)
@router.get("/", response_model=List[schemas.PhraseResponse])
def get_all_phrases(db: Session = Depends(database.get_db)):
    phrases = db.query(models.Phrase).all()
    return phrases
