from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
import random

from models import Phrase
from schemas import PhraseResponse
from dependencies import get_session

app = FastAPI(title="AlphaSort API")

@app.get("/phrase/random", response_model=PhraseResponse)
def get_random_phrase(session: Session = Depends(get_session)):
    # Get total count of phrases
    total = session.query(func.count(Phrase.uuid)).scalar()
    # Generate random offset
    random_offset = random.randint(0, total - 1)
    # Get random phrase
    phrase = session.query(Phrase).offset(random_offset).first()
    return phrase
