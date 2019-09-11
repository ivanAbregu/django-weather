import json
from unittest import TestCase, main

from .weatherApi import WeatherApi, WAConsumerAPIException

class TestWA(TestCase):
    """docstring for TestWA"""
    def setUp(self):
        pass
    
    def test_fetch_accuweather(self):
        weatherapi = WeatherApi()
        result = weatherapi.accuweather(-76.231686, -6.339848)
        print(result)
        self.assertNotEqual(result, None)
    
    def test_fetch_noaa(self):
        weatherapi = WeatherApi()
        result = weatherapi.noaa(-76.231686, -6.339848)
        print(result)
        self.assertNotEqual(result, None)

    def test_fetch_weatherdotcom(self):
        weatherapi = WeatherApi()
        result = weatherapi.weatherdotcom(-76.231686, -6.339848)
        print(result)
        self.assertNotEqual(result, None)
if __name__ == '__main__':
    main()