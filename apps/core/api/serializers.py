from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
   """Weather data serializer."""
   average = serializers.DecimalField(max_digits=5, decimal_places=2)