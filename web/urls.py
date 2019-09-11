from django.contrib import admin
from django.urls import path
from apps.core.api.views import WeatherView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/', WeatherView.as_view(), name='weather')
]
