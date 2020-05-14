from main import Weather
from unittest.mock import patch, Mock
import unittest
import requests
from os import environ

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.app = Weather("key")

    @patch("builtins.input")
    def test_api_integration(self,landon):
        # arrange
        landon.side_effect = ["London"]
        self.app = Weather(environ.get("WEATHER_API"))
        expected_response = 200
        #act
        actual = self.app.get_weather_json() 
        # assert
        self.assertEqual(expected_response, actual["cod"])
        
    @patch("builtins.input")
    def test_get_user_input(self, inputy):
        # arrange
        inputy.side_effect = ["Cairo"]
        expected = "Cairo"
        # act
        actual = self.app.get_user_input()
        # assert
        self.assertEqual(expected, actual)

    @patch("main.Weather.get_user_input", return_value=unittest.mock)    
    def test_url_builder(self, inputy):
        # arrange
        inputy.return_value = "London"
        expected = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=key"
        # act
        actual = self.app.url_builder()
        # assert
        self.assertEqual(expected, actual)
        inputy.assert_called_once()
    
    @patch("builtins.print", return_value=None)
    @patch("main.Weather.get_weather_json", return_value=unittest.mock)
    @patch("main.Weather.get_wind_dir", return_value=unittest.mock)
    @patch("main.Weather.day_perc", return_value=unittest.mock)
    def test_weather_check(self, day, dire, jason, printy):
        # arrange
        jason.return_value = {"main": {"temp": 284.47}, "sys": {"sunrise": 5,"sunset": 15894854}, "name": "London","wind": {"speed": 1000.11, "deg": 10}}
        dire.return_value = "northerly"
        day.return_value = "12.3%"
        expected = f"Location: London\nTemp: 11.32\nWind: 2237.25; northerly\nPercentage Daylight: 12.3%"
        # actual
        actual = self.app.weather_check()
        # assert
        self.assertEqual(expected, actual)
        jason.assert_called_once()
        dire.assert_called_once_with(10, 2237.25)

    def test_wind_dir_n(self):
        expected = "northerly"
        actual = self.app.get_wind_dir(11,11)
        self.assertEqual(expected,actual)

    def test_wind_dir_e(self):
        expected = "easterly"
        actual = self.app.get_wind_dir(91,91)
        self.assertEqual(expected,actual)

    def test_wind_dir_w(self):
        expected = "westerly"
        actual = self.app.get_wind_dir(271,271)
        self.assertEqual(expected,actual)
    
    def test_wind_dir_s(self):
        expected = "southerly"
        actual = self.app.get_wind_dir(180,180000000)
        self.assertEqual(expected,actual)

    def test_no_wind(self):
        expected = "calm bruv"
        actual = self.app.get_wind_dir(35,0)
        self.assertEqual(expected,actual)

    @patch("main.Weather.url_builder", return_value=unittest.mock)
    @patch("main.requests.Response", return_value=unittest.mock)
    @patch("main.requests.get", return_value=unittest.mock)
    def test_get_weather_jason(self, get, repondez, urly):
        expected = {"cod": 200}
        urly.return_value = "urly"
        get.return_value = repondez
        repondez.json.return_value = {"cod": 200}
        actual = self.app.get_weather_json()
        self.assertEqual(expected, actual)
        urly.assert_called_once()
        get.assert_called_once_with("urly")

    def test_day_perc(self):
        expected = "64.9%"
        actual = self.app.day_perc(1589429379, 1589485454)
        self.assertEqual(expected, actual)
#  def get_weather_json(self):
#         url = self.url_builder()
#         response = requests.get(url).json # Returns a requests.Response class 
#         .json() # returns json
#         print(response)
#         return response