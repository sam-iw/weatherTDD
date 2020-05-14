import requests
from os import environ

url = "https://api.openweathermap.org/data/2.5/weather?"

class Weather:

    def __init__(self, key):
        self.key = key

    def get_weather_json(self):
        url = self.url_builder()
        response = requests.get(url).json()
        # print(response)
        return response

    def get_user_input(self):
        location = input("were r u lookin 4 m8? ")
        return location

    def url_builder(self):
        location = self.get_user_input()
        return (f"{url}q={location}&appid={self.key}")

    def get_wind_dir(self, degz, fast):
        if fast == 0:
            return "calm bruv"
        elif degz in range(0,45) or degz in range(315,360):
            return "northerly"
        elif degz in range (45,135):
            return "easterly"
        elif degz in range(225, 315):
            return "westerly"
        else:
            return "southerly"
            
    def weather_check(self):
        jason = self.get_weather_json()
        locy = jason["name"]
        tempy = round(jason["main"]["temp"]-273.15,2)
        windy = round(jason["wind"]["speed"]*2.237,2)
        windy_degz = jason["wind"]["deg"]
        sunrise = jason["sys"]["sunrise"]
        sunset = jason["sys"]["sunset"]
        perc = self.day_perc(sunrise, sunset)
        diry = self.get_wind_dir(windy_degz,windy)
        whether = f"Location: {locy}\nTemp: {tempy}\nWind: {windy}; {diry}\nPercentage Daylight: {perc}"
        print(whether)
        return whether

    def day_perc(self, sunrise, sunset):
        return f"{round((sunset - sunrise)/(24*60*60)*100, 2)}%"


    
         

# app = Weather(environ.get("WEATHER_API"))
# app.weather_check()