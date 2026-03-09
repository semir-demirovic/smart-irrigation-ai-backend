import requests

def get_weather():
    """Fetches real weather data for Sarajevo using Open-Meteo (No API Key required)"""
    # Coordinates for Sarajevo
    lat = 43.8563
    lon = 18.4131
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data.get("current_weather", {})
            
            temp = current.get("temperature", 0.0)
            
            # Open-Meteo uses weather codes, we will just pass it as description
            weather_code = current.get("weathercode", 0)
            
            return {
                "temperature": float(temp),
                "rain_probability": 0.0,  # Open-meteo current doesn't provide rain prob, defaulting to 0
                "description": f"Weather code {weather_code}"
            }
            
        # Fallback if the API is down
        return {"temperature": 15.0, "rain_probability": 0.0, "description": "API response error"}
        
    except Exception as e:
        # Fallback if there is no internet connection
        return {"temperature": 15.0, "rain_probability": 0.0, "description": f"Connection error: {str(e)}"}