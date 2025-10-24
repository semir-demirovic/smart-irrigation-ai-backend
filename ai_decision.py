import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_recommendation(moisture, weather):
    """Using AI to make irrigation decisions"""
    prompt = f"""
    Soil moisture is {moisture}% and the weather forecast is {weather}.
    Should irrigation be activated? Answer YES or NO with a short reason.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"].strip()
