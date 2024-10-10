import requests
from django.shortcuts import render

def home(request):
    city = request.GET.get('city')
    data = None

    if city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=889cc1baebbffa4ddb71385cbbafccf7'
        response = requests.get(url).json()

        if response.get('cod') != '404':  # Check if city is found
            payload = {
                'city': response['name'],
                'weather': response['weather'][0]['main'],
                'icon': response['weather'][0]['icon'],
                'kelvin_temperature': response['main']['temp'],
                'celsius_temperature': round((response['main']['temp'] - 273.15), 2),  # Use 273.15 for conversion
                'pressure': response['main']['pressure'],
                'humidity': response['main']['humidity'],
                'description': response['weather'][0]['description']
            }
            data = payload

    context = {'data': data}
    return render(request, 'index.html', context)
