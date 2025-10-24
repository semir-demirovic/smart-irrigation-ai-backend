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

smart-irrigation-ai-backend/
│
├── sensors.py
├── weather_service.py
├── ai_decision.py
├── main.py
├── requirements.txt
├── .env.example
├── moisture.csv
└── README.md


---

## ⚡ Run Locally
Here's how to run the project locally, either in IntelliJ, VS Code, or the terminal:

### 1️⃣ Clone repository
```bash
git clone https://github.com/semir-demirovic/smart-irrigation-ai-backend.git
cd smart-irrigation-ai-backend

2️⃣ Create a virtual environment

The virtual environment is to install all Python libraries for this project only.

python -m venv venv

3️⃣ Activate it

    Windows:

venv\Scripts\activate

Mac/Linux:

    source venv/bin/activate

4️⃣ Install dependencies

All required libraries are in requirements.txt.

pip install -r requirements.txt

5️⃣ Create an .env file

Copy .env.example → .env and enter your OpenWeatherMap API key:

OPENWEATHER_API_KEY=here_your_api_key

6️⃣ Start the application

Start the backend server:

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000

🧠 Example Decision Flow
Soil Moisture	Rain Probability	Temperature	AI Decision
30%	0%	23°C	Irrigate now
65%	60%	18°C	No irrigation
45%	10%	28°C	Wait and recheck
🔮 Future Improvements

    Integracija sa pravim IoT senzorima (ESP32/Arduino)

    Prediktivna analiza vlage (AI model)

    Frontend dashboard (React/Flutter)

    Pohrana historijskih podataka (SQLite/PostgreSQL)

    Automatski raspored zalijevanja po parcelama

👨‍💻 Author

Semir Demirović
Backend & Java Developer | Automation & AI Enthusiast
📍 Bosnia & Herzegovina

🔗 [LinkedIn](https://www.linkedin.com/in/semir-demirovic/)

🔗 [GitHub](https://github.com/semir-demirovic/)

🪶 License

This project is open-source and available under the MIT License.


🌍 Acknowledgements

FastAPI Documentation

OpenWeatherMap API

OpenAI Platform

Pandas Library

