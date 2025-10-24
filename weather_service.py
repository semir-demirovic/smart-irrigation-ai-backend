import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    """Returning simple description of the current weather and temperature"""
    city = "Sarajevo"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"].capitalize()
    return f"{description}, {temp}°C"
