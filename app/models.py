from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship

from app.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    duration_nights = Column(Integer, nullable=False)
    is_recommended = Column(Boolean, default=False)
    
    days = relationship("Day", back_populates="itinerary", cascade="all, delete-orphan")

class Day(Base):
    __tablename__ = "days"
    
    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    
    itinerary = relationship("Itinerary", back_populates="days")
    accommodation = relationship("Accommodation", back_populates="day", uselist=False, cascade="all, delete-orphan")
    transfers = relationship("Transfer", back_populates="day", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="day", cascade="all, delete-orphan")

class Accommodation(Base):
    __tablename__ = "accommodations"
    
    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    day_id = Column(Integer, ForeignKey("days.id"))
    
    day = relationship("Day", back_populates="accommodation")

class Transfer(Base):
    __tablename__ = "transfers"
    
    id = Column(Integer, primary_key=True, index=True)
    from_location = Column(String, nullable=False)
    to_location = Column(String, nullable=False)
    transfer_type = Column(String, nullable=False)  # e.g., car, boat, etc.
    day_id = Column(Integer, ForeignKey("days.id"))
    
    day = relationship("Day", back_populates="transfers")

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    location = Column(String, nullable=False)
    duration_hours = Column(Float, nullable=False)
    day_id = Column(Integer, ForeignKey("days.id"))
    
    day = relationship("Day", back_populates="activities")