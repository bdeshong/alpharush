from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import random

from models import Phrase
from schemas import PhraseResponse
from dependencies import get_session

router = APIRouter(
    prefix="/phrase",
    tags=["phrase"]
)

@router.get("/random", response_model=PhraseResponse)
def get_random_phrase(session: Session = Depends(get_session)):
    # Get total count of phrases
    total = session.query(func.count(Phrase.uuid)).scalar()
    # Generate random offset
    random_offset = random.randint(0, total - 1)
    # Get random phrase
    phrase = session.query(Phrase).offset(random_offset).first()
    return phrase
