from sqlalchemy.orm import Session
from app import crud

def get_recommended_itineraries(db: Session, duration_nights: int):
    return crud.get_recommended_itineraries(db, duration_nights)