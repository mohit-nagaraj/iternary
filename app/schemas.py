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
    id: Optional[int] = None  
    day_id: int
    
    class Config:
        from_attributes = True  

class TransferBase(BaseModel):
    from_location: str
    to_location: str
    transfer_type: str

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: Optional[int] = None  
    day_id: int
    
    class Config:
        from_attributes = True  

class AccommodationBase(BaseModel):
    hotel_name: str
    location: str

class AccommodationCreate(AccommodationBase):
    pass

class Accommodation(AccommodationBase):
    id: Optional[int] = None  
    day_id: int
    
    class Config:
        from_attributes = True  

class DayBase(BaseModel):
    day_number: int

class DayCreate(DayBase):
    accommodation: Optional[AccommodationCreate] = None
    transfers: List[TransferCreate] = []
    activities: List[ActivityCreate] = []

class Day(DayBase):
    id: Optional[int] = None  
    itinerary_id: int
    accommodation: Optional[Accommodation] = None
    transfers: List[Transfer] = []
    activities: List[Activity] = []
    
    class Config:
        from_attributes = True  

class ItineraryBase(BaseModel):
    name: str
    destination: str
    duration_nights: int

class ItineraryCreate(ItineraryBase):
    days: List[DayCreate]
    is_recommended: Optional[bool] = False

class Itinerary(ItineraryBase):
    id: Optional[int] = None  
    days: List[Day] = []
    is_recommended: bool
    
    class Config:
        from_attributes = True  

class RecommendedItineraryRequest(BaseModel):
    duration_nights: int