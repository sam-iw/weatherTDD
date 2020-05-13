from main import Weather
from unittest.mock import patch
import unittest
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
    
    @patch("main.Weather.url_builder", return_value=unittest.mock)
    @patch("main.Weather.get_user_input", return_value=unittest.mock)
    @patch("main.Weather.get_weather_json", return_value=unittest.mock)
    def test_weather_check(self, jason, inputy, urly):
        # arrange
        urly.return_value = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=key"
        inputy.return_value = "London"
        jason.return_value = {"main": {"temp": 284.47}, "name": "London","wind": {"speed": 1000.11, "deg": 10}}
        expected = f"Location: London\nTemp: 11.32\nWind: 2237.25; northerly"

        # actual
        actual = self.app.weather_check()

        # assert
        self.assertEqual(expected, actual)

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