from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from database import Base

class Crop(Base):
    """Represents a specific plant type in the orchard"""
    __tablename__ = "crops"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True) # e.g., "Apple Tree", "Plum Tree"
    optimal_moisture = Column(Float)   # Ideal moisture level for this specific crop
    
    # Relationship with logs
    logs = relationship("IrrigationLog", back_populates="crop")

class IrrigationLog(Base):
    """Stores every irrigation decision and sensor reading"""
    __tablename__ = "irrigation_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    soil_moisture = Column(Float)
    temperature = Column(Float)
    ai_decision = Column(String)
    
    # Foreign key to associate the log with a specific crop
    crop_id = Column(Integer, ForeignKey("crops.id"))
    crop = relationship("Crop", back_populates="logs")