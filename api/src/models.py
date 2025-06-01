from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Phrase(Base):
    __tablename__ = "phrase"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, nullable=False, index=True)
    phrase = Column(String(255), nullable=False)
    created = Column(DateTime, default=func.now(), nullable=False)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __init__(self, **kwargs):
        if 'uuid' not in kwargs:
            kwargs['uuid'] = str(uuid.uuid4())
        super().__init__(**kwargs)
