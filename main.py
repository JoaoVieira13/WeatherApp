import sys
from services.weather_service import fetch_weather, process_weather

def get_user_input():
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        return lat, lon
    except ValueError:
        print("Invalid input, please enter numeric values.")
        sys.exit(1)

def display_weather(temp, wind, condition):
    print("\n--- Current Weather ---")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {wind} km/h")
    print(f"Condition: {condition}")

def main():
    lat, lon = get_user_input()
    data = fetch_weather(lat, lon)
    temp, wind, condition = process_weather(data)
    display_weather(temp, wind, condition)

if __name__ == "__main__":
    main()