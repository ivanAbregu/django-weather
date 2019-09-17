from .weatherApi import WeatherApi
import statistics
def is_valid_latitude(value):
    result = False
    try:
        result = value!=None and float(value) < 90 and float(value) > -90
    except:
        pass
    return result
def is_valid_longitude(value):
    result = False
    try:
        result = value!=None and float(value) < 180 and float(value) > -180
    except:
        pass
    return result

def get_average(latitude, longitude, accuweather, noaa, weatherdotcom):
    """Function to fetch the weather services and calculate the average"""

    list_weathers = []
    weatherapi = WeatherApi()
    if accuweather != None:
        res = weatherapi.accuweather(latitude,longitude)
        res = weatherapi.parse_accuweather(res)
        list_weathers.append(res)
    if noaa != None:
        res = weatherapi.noaa(latitude,longitude)
        res = weatherapi.parse_noaa(res)
        list_weathers.append(res)
    if weatherdotcom != None:
        res = weatherapi.weatherdotcom(latitude,longitude)
        res = weatherapi.parse_weatherdotcom(res)
        list_weathers.append(res)
    return statistics.mean(list_weathers)