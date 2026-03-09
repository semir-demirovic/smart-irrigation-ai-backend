import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_recommendation(moisture, weather):
    """
    Uses AI to make irrigation decisions based on soil moisture and weather data.
    Includes a fallback mechanism if the API key is missing or service is down.
    """
    
    # Fallback logic: If OpenAI key is missing or using placeholder, use hardcoded logic
    if not openai.api_key or openai.api_key == "your_openai_api_key_here":
        if moisture < 40:
            return "YES - Mocked decision: Soil is too dry."
        return "NO - Mocked decision: Moisture is sufficient."

    # Construct the prompt for the AI model
    prompt = f"""
    Soil moisture is {moisture}% and the weather forecast is {weather}.
    Should irrigation be activated? Answer YES or NO with a short reason.
    """
    
    try:
        # Call the OpenAI API using the GPT-3.5 Turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        # Error handling for API service interruptions
        return f"Error: AI service unavailable ({str(e)})"