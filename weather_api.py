from typing import Final
import os
import requests



API_KEY: Final[str] = os.environ['OPEN_WEATHER_API_KEY']
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock: 
        with open('dummy_data.json') as file:
            return json.load(file)
        

        # request live data
        payload: dict = {'q': city_name, 'appid': API_key, 'units': 'metric'}
        request = requests.get(url=BASE_URL, params=payload)
        data: dict = request.json

        return data
    

    