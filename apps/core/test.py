from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class AuthTest(APITestCase):
    def setUp(self):
        self.url = '/api/weather/'

    def test_accuweather(self):
        payload = {'latitude': 44, 'longitude': 33,'accuweather':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_noaa(self):
        payload = {'latitude': 44, 'longitude': 33,'noaa':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_weatherdotcom(self):
        payload = {'latitude': 44, 'longitude': 33,'weatherdotcom':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_average2(self):
        payload = {'latitude': 44, 'longitude': 33,'noaa':'','weatherdotcom':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_average3(self):
        payload = {
                    'latitude': 44,
                    'longitude': 33,
                    'noaa':'',
                    'weatherdotcom':'',
                    'accuweather':''
                }
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missing_param(self):
        payload = {'latitude': 33,'noaa':'','weatherdotcom':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_filters(self):
        payload = {'latitude': 44, 'longitude': 33}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_bad_param(self):
        payload = {'latitude': -91, 'longitude': 33,'noaa':'','weatherdotcom':''}
        response = self.client.get(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)