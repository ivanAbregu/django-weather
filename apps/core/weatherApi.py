from __future__ import absolute_import, unicode_literals
import os
import logging
import requests
import json

logger = logging.getLogger('weather-api')

BASE_DOMAIN = os.environ.get('WA_URL','http://127.0.0.1:5000/')

class WAConsumerAPIException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = kwargs.get('message', "")
        self.error_code = kwargs.get('error_code', "")
        self.kwargs = kwargs
        logger.debug(
            "WeatherApi Consumer API Exceiption %s" % kwargs)

    @property
    def json(self):
        return self.kwargs


def handler_req_except():
    def decorate(func):
        def call(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except requests.ConnectTimeout as e:
                raise WAConsumerAPIException(**{
                    'message': 'Conection Timeout',
                    'function': 'WeatherApi',
                    'error_code': "-",
                    'raw_response': e
                })
            except requests.ConnectionError as e:
                raise WAConsumerAPIException(**{
                    'message': 'Conection Error',
                    'function': 'WeatherApi',
                    'error_code': "-",
                    'raw_response': e
                })

        return call
    return decorate

class WeatherApi(object):
    """
        WeatherApi system Connection class
    """

    def __init__(self, *args, **kwargs):
        pass
    def get_default_header(self):
        """
        Return default header for consumer WeatherApi api
        """
        return {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

    @handler_req_except()
    def accuweather(self,latitude,longitude):
        """
        Get weather from accuweather
        """
        url = BASE_DOMAIN + 'accuweather'
        payload = {'latitude': latitude, 'longitude': longitude}
        response = requests.get(url, params=payload )
        # return response
        if response.status_code == 200:
            data = response.json()
            logger.debug("WeatherApi accuweather %s " % response.text)
            return data
        else:
            raise WAConsumerAPIException(**{
                'message': response.json(),
                'function': 'accuweather',
                'error_code': data.get('result', '-'),
                'raw_response': data
            })

    @handler_req_except()
    def noaa(self,latitude,longitude):
        """
        Get weather from GET noaa
        """
        url = BASE_DOMAIN + 'noaa'
        payload = {'latlon': f'{latitude},{longitude}'}
        response = requests.get(url, params=payload )
        # return response
        if response.status_code == 200:
            data = response.json()
            logger.debug("WeatherApi noaa %s " % response.text)
            return data
        else:
            raise WAConsumerAPIException(**{
                'message': response.json(),
                'function': 'noaa',
                'error_code': data.get('result', '-'),
                'raw_response': data
            })
    @handler_req_except()
    def weatherdotcom(self,latitude,longitude):
        """
        Get weather from GET weatherdotcom
        """
        url = BASE_DOMAIN + 'weatherdotcom'
        body = {'lat': latitude, 'lon': longitude}
        response = requests.post(url, json=body)
        # return response
        if response.status_code == 200:
            data = response.json()
            logger.debug("WeatherApi weatherdotcom %s " % response.text)
            return data
        else:
            raise WAConsumerAPIException(**{
                'message': response.json(),
                'function': 'weatherdotcom',
                'error_code': data.get('result', '-'),
                'raw_response': data
            })

    @handler_req_except()
    def parse_accuweather(self, data):
        try:
            return float(data['simpleforecast']['forecastday'][0]['current']['fahrenheit'])
        except Exception as e:
             logger.debug("parse_accuweather Exceiption %s" % e)
             raise e

    @handler_req_except()
    def parse_noaa(self, data):
        try:
            return float(data['today']['current']['fahrenheit'])
        except Exception as e:
             logger.debug("parse_noaa Exceiption %s" % e)
             raise e
    
    @handler_req_except()
    def parse_weatherdotcom(self, data):
        try:
            return float(data['query']['results']['channel']['condition']['temp'])
        except Exception as e:
             logger.debug("parse_weatherdotcom Exceiption %s" % e)
             raise e
