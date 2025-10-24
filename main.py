from fastapi import FastAPI
from sensors import get_moisture_data
from weather_service import get_weather
from ai_decision import get_ai_recommendation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Irrigation AI System Running"}

@app.get("/irrigate")
def irrigate():
    moisture = get_moisture_data()
    weather = get_weather()
    ai_decision = get_ai_recommendation(moisture, weather)
    return {
        "sensor_moisture": moisture,
        "weather": weather,
        "AI_decision": ai_decision
    }
