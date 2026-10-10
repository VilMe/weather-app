from weather_api import get_weather, get_weather_details, Weather

def main():
    user_city: str = input('Enter a city: ')

    # Get the current weather details
    current_weather: dict = get_weather(user_city, mock=True)
    weather_details: list[Weather] = get_weather_details(current_weather)

    # Get the current days
    dfmt: str = '%d/%m/%y'
    days: list[str] = (list({f'{date.date:{dfmt}}' for date in weather_details}))