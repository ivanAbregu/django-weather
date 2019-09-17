from rest_framework import views, status
from rest_framework.response import Response
from ..weatherApi import WeatherApi, WAConsumerAPIException
from .serializers import WeatherSerializer
import statistics
from ..utils import get_average,is_valid_latitude, is_valid_longitude

class WeatherView(views.APIView):
    """API Weather. Allowed method GET"""

    def get(self, request):
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        accuweather = self.request.query_params.get('accuweather', None)
        noaa = self.request.query_params.get('noaa', None)
        weatherdotcom = self.request.query_params.get('weatherdotcom', None)
        if not( is_valid_latitude(latitude) and is_valid_longitude(longitude) ):
            return Response(
                {'message': 'latitude and longitude are required.'},
                status=status.HTTP_400_BAD_REQUEST)

        if accuweather==None and noaa==None and weatherdotcom==None:
            return Response(
                {'message': 'At least one filter is required. [accuweather, noaa, weatherdotcom]'},
                status=status.HTTP_400_BAD_REQUEST)
        
        try:
            """obtain the average weather"""
            mean = get_average(latitude, longitude, accuweather, noaa, weatherdotcom)
            content = WeatherSerializer({'average':mean}).data
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(content)