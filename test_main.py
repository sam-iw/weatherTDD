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
    def test_get_usinput(self, inputy):
        # arrange
        inputy.side_effect = ["London"]
        expected = "London"
        # act
        actual = self.app.get_user_input()
        # assert
        self.assertEqual(expected, actual)