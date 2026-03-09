from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, get_db, SessionLocal
from sensors import get_moisture_data
from weather_service import get_weather
from ai_decision import get_ai_recommendation

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database seed: Add initial crops on startup if the table is empty
@app.on_event("startup")
def setup_db():
    db = SessionLocal()
    if not db.query(models.Crop).first():
        apple = models.Crop(name="Apple Trees", optimal_moisture=60.0)
        plum = models.Crop(name="Plum Trees", optimal_moisture=50.0)
        db.add_all([apple, plum])
        db.commit()
    db.close()

@app.get("/irrigate/{crop_id}")
def irrigate_crop(crop_id: int, db: Session = Depends(get_db)):
    """Triggers irrigation decision logic for a specific crop ID"""
    crop = db.query(models.Crop).filter(models.Crop.id == crop_id).first()
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
        
    moisture = get_moisture_data()
    weather_data = get_weather()
    
    # AI logic considers the specific crop's optimal moisture
    context = f"Crop: {crop.name}, Target Moisture: {crop.optimal_moisture}, Weather: {weather_data}"
    ai_decision = get_ai_recommendation(moisture, context)
    
    # Persist data to the database
    new_log = models.IrrigationLog(
        soil_moisture=float(moisture),
        temperature=float(weather_data.get("temperature", 0.0)),
        ai_decision=ai_decision,
        crop_id=crop.id
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    
    return {
        "crop": crop.name,
        "current_moisture": moisture,
        "target": crop.optimal_moisture,
        "weather": weather_data,
        "ai_decision": ai_decision,
        "log_id": new_log.id
    }

@app.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    """Retrieves the last 10 irrigation logs including crop data"""
    logs = db.query(models.IrrigationLog).order_by(models.IrrigationLog.id.desc()).limit(10).all()
    return logs