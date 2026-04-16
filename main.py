import sys
from services.weather_service import fetch_weather, process_weather
from web.app import run_web_app

def cli_mode():
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))

    data = fetch_weather(lat, lon)
    temp, wind, condition = process_weather(data)

    print("\n--- Current Weather ---")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {wind} km/h")
    print(f"Condition: {condition}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--web":
        run_web_app()
    else:
        cli_mode()