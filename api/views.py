import os
import requests
from django.http import JsonResponse

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    provided_city = request.GET.get('city')

    # Get client IP
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    try:
        if provided_city:
            city = provided_city
        else:
            # Get location info based on IP
            location_response = requests.get(f'http://ipinfo.io/{client_ip}/json')
            location_data = location_response.json()

            # Debugging information
            print(f"IP Info Response: {location_data}")

            city = location_data.get('city', 'Unknown City')

        if city == 'Unknown City' or 'bogon' in location_data:
            city = 'Unknown City'  # Default city as fallback
            print(f"Using default city: {city}")

        # Get weather info
        weather_response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=5d283a99d22ce2b152ec51514eb42a88'
        )
        weather_data = weather_response.json()

        # Debugging information
        print(f"Weather API Response: {weather_data}")

        if 'main' not in weather_data:
            response = {
                "client_ip": client_ip,
                "location": "Unknown City",
                "greeting": f"Hello, {visitor_name}!, the temperature is N/A degrees Celsius in Unknown City "
            }
        else:
            temperature = weather_data['main']['temp']
            response = {
                "client_ip": client_ip,
                "location": city,
                "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
            }
    except Exception as e:
        response = {"error": str(e)}

    return JsonResponse(response)
