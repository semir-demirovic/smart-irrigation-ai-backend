# 🌾 Smart Irrigation AI Backend

### Intelligent Water Management System using Python, FastAPI & OpenAI

---

## 🧠 Overview

Smart Irrigation AI Backend is a prototype system designed to automate agricultural irrigation using real-time sensor data, weather information, and simple AI-based decision logic.  
The goal of the project is to **optimize water usage** and **reduce manual intervention** in crop management through automated decision-making.

The system collects soil moisture readings from CSV files (or sensors), fetches live weather data via API, and makes irrigation decisions based on both factors.  
A lightweight **FastAPI backend** exposes REST endpoints and can be easily extended for IoT or frontend integration.

---

## ⚙️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **AI/Logic:** OpenAI GPT API (for intelligent irrigation reasoning)
- **Data Handling:** CSV (Pandas)
- **Weather API:** OpenWeatherMap
- **Environment Variables:** python-dotenv
- **Testing:** HTTP requests via FastAPI TestClient

---

## 🚀 How It Works

1. **Sensors Module (`sensors.py`)**  
   - Reads real or simulated soil moisture data from `moisture.csv`.  
   - Provides moisture values for AI decision-making.

2. **Weather Module (`weather_service.py`)**  
   - Fetches current weather data (temperature, humidity, rain probability) from the OpenWeatherMap API.

3. **AI Decision Engine (`ai_decision.py`)**  
   - Uses OpenAI GPT logic to combine moisture + weather data and decide whether irrigation is needed.

4. **Main Backend (`main.py`)**  
   - FastAPI endpoints for checking system status, current irrigation decision, and sensor simulation.  
   - Can be expanded to handle IoT or MQTT sensor inputs.

---

## 🧩 Project Structure

