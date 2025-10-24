#  Smart Irrigation AI Backend

## Overview

This project demonstrates how **AI** and **Python (FastAPI)** can automate irrigation decisions  
based on **soil moisture sensor data** and **weather forecasts**.

It’s a small but realistic backend that connects **IoT + AI + Weather API**,  
mimicking a real-world smart agriculture use case.

---

## Tech Stack

| Component | Description |
|------------|--------------|
| 🐍 Python 3.11 | Core language |
| ⚡ FastAPI | REST backend |
| ☁️ OpenWeatherMap API | Weather data |
| 🤖 OpenAI API | AI-based decisions |
| 📊 Pandas | Sensor data handling |
| 🧱 dotenv | Config management |
| 🔄 Uvicorn | Local development server |

---

## ⚙️ How It Works

1. Reads the latest **soil moisture** value from a CSV file.
2. Fetches **weather conditions** from OpenWeatherMap API.
3. Sends both inputs to **OpenAI API** which decides if irrigation is needed.
4. Returns a JSON response like this:

```json
{
  "sensor_moisture": 38,
  "weather": "Cloudy, 21°C",
  "AI_decision": "YES - Soil is too dry, irrigation needed."
}
