from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import phrase
from config import settings

app = FastAPI(title="AlphaSort API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(phrase.router)
