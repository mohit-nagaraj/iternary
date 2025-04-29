from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas

def get_itinerary(db: Session, itinerary_id: int):
    return db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()

def get_itineraries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Itinerary).offset(skip).limit(limit).all()

def get_recommended_itineraries(db: Session, duration_nights: int):
    return db.query(models.Itinerary).filter(
        models.Itinerary.is_recommended == True,
        models.Itinerary.duration_nights == duration_nights
    ).all()

def create_itinerary(db: Session, itinerary: schemas.ItineraryCreate):
    db_itinerary = models.Itinerary(
        name=itinerary.name,
        destination=itinerary.destination,
        duration_nights=itinerary.duration_nights,
        is_recommended=itinerary.is_recommended
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    
    for day_data in itinerary.days:
        db_day = models.Day(day_number=day_data.day_number, itinerary_id=db_itinerary.id)
        db.add(db_day)
        db.commit()
        db.refresh(db_day)
        
        if day_data.accommodation:
            db_accommodation = models.Accommodation(
                hotel_name=day_data.accommodation.hotel_name,
                location=day_data.accommodation.location,
                day_id=db_day.id
            )
            db.add(db_accommodation)
        
        for transfer_data in day_data.transfers:
            db_transfer = models.Transfer(
                from_location=transfer_data.from_location,
                to_location=transfer_data.to_location,
                transfer_type=transfer_data.transfer_type,
                day_id=db_day.id
            )
            db.add(db_transfer)
        
        for activity_data in day_data.activities:
            db_activity = models.Activity(
                name=activity_data.name,
                description=activity_data.description,
                location=activity_data.location,
                duration_hours=activity_data.duration_hours,
                day_id=db_day.id
            )
            db.add(db_activity)
    
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary