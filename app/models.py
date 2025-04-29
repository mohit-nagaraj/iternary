from typing import List, Optional
from pydantic import BaseModel

class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: str
    duration_hours: float

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    day_id: int
    
    class Config:
        orm_mode = True

class TransferBase(BaseModel):
    from_location: str
    to_location: str
    transfer_type: str

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: int
    day_id: int
    
    class Config:
        orm_mode = True

class AccommodationBase(BaseModel):
    hotel_name: str
    location: str

class AccommodationCreate(AccommodationBase):
    pass

class Accommodation(AccommodationBase):
    id: int
    day_id: int
    
    class Config:
        orm_mode = True

class DayBase(BaseModel):
    day_number: int

class DayCreate(DayBase):
    accommodation: Optional[AccommodationCreate] = None
    transfers: List[TransferCreate] = []
    activities: List[ActivityCreate] = []

class Day(DayBase):
    id: int
    itinerary_id: int
    accommodation: Optional[Accommodation] = None
    transfers: List[Transfer] = []
    activities: List[Activity] = []
    
    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    name: str
    destination: str
    duration_nights: int

class ItineraryCreate(ItineraryBase):
    days: List[DayCreate]
    is_recommended: Optional[bool] = False

class Itinerary(ItineraryBase):
    id: int
    days: List[Day] = []
    is_recommended: bool
    
    class Config:
        orm_mode = True

class RecommendedItineraryRequest(BaseModel):
    duration_nights: int