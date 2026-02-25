from typing import Final
import os




API_KEY: Final[str] = os.environ['OPEN_WEATHER_API_KEY']
BASE_URL: Final[str] = 'api.openweathermap.org/data/2.5/forecast'