# import requests
# import json
from os import environ

url = "https://api.openweathermap.org/data/2.5/weather?"

class Weather:

    def __init__(self, key):
        self.key = key

    def get_weather_json(self):
        return {"cod":"200"}

    def get_user_input(self):
        location = input("were r u lookin 4 m8? ")
        return location

    def url_builder(self, location):
        return (f"{url}q={location}&appid={self.key}")

    