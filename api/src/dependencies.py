from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
