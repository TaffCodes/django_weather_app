from django.db import models
from django.conf import settings
import requests

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

def get_weather_data(request):
    weather_data = {}
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')

        if city:
            SearchHistory.objects.create(city=city)
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error = data.get('message', 'Error fetching weather data')

    return weather_data, error