import requests


def get_weather(city):
    api_key = "ebd05fd11c2886ab0210db8dc26132d0"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if response.status_code == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        return [weather_description, temperature]
    else:
        return None, None
