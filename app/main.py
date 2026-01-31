import os
import requests

API_KEY = os.getenv("API_KEY")

CITY = "Paris"
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather() -> None:
    if not API_KEY:
        raise RuntimeError("API_KEY environment variable is not set")

    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"Current weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")


if __name__ == "__main__":
    get_weather()
