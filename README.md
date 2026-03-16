🌾 Smart Irrigation AI Backend
Enterprise-Grade Water Management System (FastAPI, PostgreSQL, Docker & AI)

🧠 Overview
Smart Irrigation AI Backend is a robust, production-ready prototype designed to automate agricultural irrigation for a personal orchard.
Moving beyond simple scripts, this system utilizes real-time weather data API integration, simulated hardware sensors, and an AI decision engine with built-in graceful degradation. All decisions and sensor readings are persisted in a Dockerized PostgreSQL database using a relational schema to manage different crops.

🚀 Key Features & Engineering Highlights
Resilient AI Logic: Uses OpenAI for intelligent decision-making, with automated fallback algorithms if the AI service goes offline.

Zero-Key Weather Integration: Uses Open-Meteo API for real-time localization data for Sarajevo (no API keys required for local testing).

Relational Data Modeling: Implements a One-to-Many relationship between Crops (e.g., Apple Trees, Plum Trees) and Irrigation Logs.

Containerized Database: PostgreSQL database instantly deployable via Docker Compose for consistent environments.

Clean Architecture: Strict separation of concerns across modules (sensors, weather_service, ai_decision, database, models).

⚙️ Tech Stack
Backend Framework: FastAPI / Python 3.10+

Database: PostgreSQL & SQLAlchemy (ORM)

Infrastructure: Docker & Docker Compose

AI/Logic: OpenAI GPT API

External Data: Open-Meteo API

Data Handling: Pandas & SQLAlchemy Query Logic

⚡ Quick Start (Run Locally)

1️⃣ Clone the repository

Bash
git clone https://github.com/semir-demirovic/smart-irrigation-ai-backend.git
cd smart-irrigation-ai-backend

2️⃣ Start the PostgreSQL Database (via Docker)
Ensure Docker is running on your machine, then execute:

Bash
docker-compose up -d

3️⃣ Setup Python Environment

Bash
python -m venv venv
source venv/Scripts/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt

4️⃣ Run the Application

Bash
uvicorn main:app --reload

🛠 API Documentation & Testing
FastAPI automatically generates interactive documentation. Access the Swagger UI to test the system:

👉 http://127.0.0.1:8000/docs

Core Endpoints:
Trigger Irrigation Cycle: GET /irrigate/{crop_id}

Example for Apples (ID 1): http://127.0.0.1:8000/irrigate/1

Example for Plums (ID 2): http://127.0.0.1:8000/irrigate/2

View Database Logs: GET /logs (Retrieves the 10 most recent records)

Average Moisture Stats: GET /stats/{crop_id} (SQL aggregation example)

👨‍💻 Author
Semir Demirović Bachelor of Computer Science (BCompSc)
Backend Developer | Automation & AI Enthusiast

📍 Bosnia & Herzegovina

[🔗](https://www.linkedin.com/in/semir-demirovic/) LinkedIn Profile

[🔗](https://github.com/semir-demirovic/) GitHub Profile

🪶 License
This project is open-source and available under the MIT License.
