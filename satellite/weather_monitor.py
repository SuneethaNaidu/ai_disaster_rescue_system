import requests

API="YOUR_API_KEY"

def get_weather():

    url=f"https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid={API}"

    response=requests.get(url)

    return response.json()
