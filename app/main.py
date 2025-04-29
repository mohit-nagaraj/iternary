from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import itineraries

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary System",
    description="API for managing travel itineraries with recommended options",
    version="1.0.0",
)

app.include_router(itineraries.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Itinerary System"}