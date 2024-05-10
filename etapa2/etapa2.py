import requests
import json
import logging
import os
from dotenv import load_dotenv
from exceptions import CityNotFoundError, APIError


class WeatherService():
    def __init__(self):
        self.__api_key = os.getenv('API_KEY')

    def get_coordinates(self, city):
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={self.__api_key}'

        response = requests.get(url)
        print(response.status_code)
        print(response.text)

        response_data = json.loads(response.text)
        if response.status_code == 200:
            if len(response_data) == 0:
                raise CityNotFoundError(f'A cidade {city} não foi encontrada')

            lat = response_data[0]['lat']
            lon = response_data[0]['lon']

            return lat, lon
        else:
            raise APIError(response_data['message'])

    def get_weather_information(self, lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=pt_br&appid={self.__api_key}'
        response = requests.get(url)
        print(response.status_code)
        print(response.text)

        response_data = json.loads(response.text)
        if response.status_code == 200:
            description = response_data['weather'][0]['description']
            temp = response_data['main']['temp']

            return temp, description
        else:
            raise APIError(response_data['message'])


def config_logs():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s %(name)s %(lineno)d %(levelname)s %(message)s')
    file_handler = logging.FileHandler('logs.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    load_dotenv()
    try:
        logger = config_logs()
        weather_service = WeatherService()
        # city = 'Porto Alegre'
        city = input('Digite o nome da cidade: ')
        lat, lon = weather_service.get_coordinates(city)
        temp, description = weather_service.get_weather_information(lat, lon)

        print(f'Temperatura em {city}: {temp}°C - {description}')
    except (CityNotFoundError, APIError) as e:
        print(e.message)
        logger.exception(e)
    except Exception as e:
        print(e)
        logger.exception(e)
