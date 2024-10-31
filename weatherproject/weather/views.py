from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render


def weather_view(request):
    api_key = '0cf669aafb4869260a8bb6304bb42fe0'
    city = request.GET.get('city', 'London')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        context = {'city': city, 'weather': weather_data}
    else:
        context = {'city': city, 'weather': None, 'error': 'City not found!'}

    return render(request, 'weather/weather.html', context)

