import requests

API_KEY = "5d8d9c6a68a2c2725537663ced839da7"

def get_weather(city="Chennai"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        raise Exception(data)

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    rainfall = 0
    if "rain" in data:
        rainfall = data["rain"].get("1h", 0)

    return rainfall, temperature, humidity, wind
