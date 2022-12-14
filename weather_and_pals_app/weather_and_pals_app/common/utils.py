import requests
import json
import os
from datetime import datetime


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def get_weather_update(city_name):
    API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
    # the url for current weather, takes city_name and API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    # converting the request response to json
    response = requests.get(url).json()
    # getting the current time
    current_time = datetime.now()
    # formatting the time using directives, it will take this format Day, Month Date Year, Current Time
    formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    # bundling the weather information in one dictionary
    city_weather_update = {
        'city': city_name,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
        'country_code': response['sys']['country'],
        'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
        'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
        'time': formatted_time
    }
    return city_weather_update
