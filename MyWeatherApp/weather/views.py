import requests
from django.conf import settings
from django.shortcuts import render
from .models import SearchHistory
from datetime import datetime

def get_weather(request):
    weather_data = {}
    error = None

    if request.method == "POST":
        city = request.POST.get("city")
        
        if city:
            # Save the city search in history
            SearchHistory.objects.create(city = city)
            
            # Make an API call to OpenWeather
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'].capitalize(),
                    'icon': data['weather'][0]['icon'],
                    'wind_speed': data['wind']['speed'],
                    'visibility': data['visibility'],
                    'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                    'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
                }
            else:
                error = "City not found. Please try again."

    

     # Fetch and format search history dates
    history = SearchHistory.objects.all().order_by('-search_date')[:10] 
    [
        {
            'city': record.city,
            'search_date': record.search_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        for record in history
    ]

    return render(request, "weather/index.html", {'weather_data': weather_data, 'error': error, 'history': history})
