from fastapi import FastAPI
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary System",
    description="API for managing travel itineraries with recommended options",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Itinerary System"}