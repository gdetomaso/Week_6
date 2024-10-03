import os
import requests
from pprint import pprint


# Minneapolis
lat = 44.97
lon = -93.26
units = 'metric' # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.


api_key = os.environ['WEATHER_KEY'] # Set this environment variable on your computer


url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'


response = requests.get(url)
weather_forecast = response.json()


# Print the weather forecast for the next 5 days with pretty formatting
for forecast in weather_forecast['list']:
    date = forecast['dt_txt']
    temperature = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    print(f"{date}: {temperature:.1f}°C, {description}")