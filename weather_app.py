import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="weather_app")
api_key = 'API_KEY'
city_input = input('Enter city name: ')

location = geolocator.geocode(city_input)
lat = location.latitude
lon = location.longitude
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
if (weather_data.status_code == 200):
    temp = weather_data.json()['main']['temp']-273.15
    weather = weather_data.json()['weather'][0]['description']
    print(f"Tempature: {round(temp,2)} C°")
    print(f"Description: {weather}")
else:
    print("Something went wrong, please try again.")    

