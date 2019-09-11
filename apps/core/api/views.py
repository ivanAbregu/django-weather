from rest_framework import views, status
from rest_framework.response import Response
from ..weatherApi import WeatherApi, WAConsumerAPIException
from .serializers import WeatherSerializer
import statistics

class WeatherView(views.APIView):

    def get(self, request):
        results = []
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        accuweather = self.request.query_params.get('accuweather', None)
        noaa = self.request.query_params.get('noaa', None)
        weatherdotcom = self.request.query_params.get('weatherdotcom', None)

        if not(latitude and longitude):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        weatherapi = WeatherApi()
        try:
            if accuweather != None:
                res = weatherapi.accuweather(latitude,longitude)
                res = weatherapi.parse_accuweather(res)
                results.append(res)
            if noaa != None:
                res = weatherapi.noaa(latitude,longitude)
                res = weatherapi.parse_noaa(res)
                results.append(res)
            if weatherdotcom != None:
                res = weatherapi.weatherdotcom(latitude,longitude)
                res = weatherapi.parse_weatherdotcom(res)
                results.append(res)
            mean = statistics.mean(results)
            content = WeatherSerializer({'average':mean}).data
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(content)