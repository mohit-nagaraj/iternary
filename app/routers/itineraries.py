from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas
from app.database import get_db
from app.services.mcp_service import get_recommended_itineraries

router = APIRouter(
    prefix="/itineraries",
    tags=["itineraries"],
)

@router.post("/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db=db, itinerary=itinerary)

@router.get("/", response_model=List[schemas.Itinerary])
def read_itineraries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    itineraries = crud.get_itineraries(db, skip=skip, limit=limit)
    return itineraries

@router.get("/{itinerary_id}", response_model=schemas.Itinerary)
def read_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    db_itinerary = crud.get_itinerary(db, itinerary_id=itinerary_id)
    if db_itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return db_itinerary

@router.post("/recommended", response_model=List[schemas.Itinerary])
def get_recommended(request: schemas.RecommendedItineraryRequest, db: Session = Depends(get_db)):
    return get_recommended_itineraries(db, request.duration_nights)