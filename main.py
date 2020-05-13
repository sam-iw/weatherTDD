# import requests
# import json
from os import environ

class Weather:

    url = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, key):
        pass

    def get_weather_json(self):
        return {"cod":"200"}

    def get_user_input(self):
        location = input("were r u lookin 4 m8? ")
        return "London"