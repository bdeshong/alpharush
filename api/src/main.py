from fastapi import FastAPI
from routers import phrase

app = FastAPI(title="AlphaSort API")

app.include_router(phrase.router)
