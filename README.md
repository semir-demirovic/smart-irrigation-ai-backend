# Smart Irrigation AI Backend

This project demonstrates how **AI and Python** can automate irrigation decisions
based on **sensor data** and **weather forecasts**.

Built with:
- FastAPI (for API)
- OpenAI API (AI-based decision)
- OpenWeatherMap API (weather data)
- Pandas for CSV sensor reading

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
