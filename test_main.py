from main import Weather
from unittest.mock import patch
import unittest

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.app = Weather("key")

    def test_api_integration(self):
        # arrange
        expected_response = "200"
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
        jason.return_value = {"main": {"temp": 284.47}}
        expected = f"Location: London\nTemp: 284.47"

        # actual
        actual = self.app.weather_check()

        # assert
        self.assertEqual(expected, actual)
        