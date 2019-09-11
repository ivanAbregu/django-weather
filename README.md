# Django-weather-api
Test Django

### Setup
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver

```

### Routes
Host: http://127.0.0.1:8000/
##### API
GET /api/weather/
###### params 
```
required: latitude, longitude.
filters: accuweather, noaa and weatherdotcom.
```
###### Example
http://127.0.0.1:8000/api/weather/?accuweather&noaa&weatherdotcom&latitude=-78.416226&longitude=-5.717964


