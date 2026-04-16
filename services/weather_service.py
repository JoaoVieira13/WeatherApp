import requests
import sys
from utils.weather_codes import WEATHER_DESCRIPTIONS

def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("Error fetching data from API.")
        sys.exit(1)

def process_weather(data):
    if "current_weather" not in data:
        print("Weather data not available.")
        sys.exit(1)

    weather = data["current_weather"]

    temperature = weather.get("temperature")
    windspeed = weather.get("windspeed")
    weathercode = weather.get("weathercode")

    condition = WEATHER_DESCRIPTIONS.get(weathercode, "Unknown")

    return temperature, windspeed, condition