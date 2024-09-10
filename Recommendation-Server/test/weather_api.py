import requests

lat = 23.4643
lon = 73.2988

API_key = '971810551b940ca1527c328414526456'
web = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

# get the weather data
weather_data = requests.get(web)
weather_data = weather_data.json()

# get the temperature
Temperature = weather_data['main']['temp']
# convert temperature from kelvin to celsius
Temperature = Temperature - 273.15

# get the humidity
Humidity = weather_data['main']['humidity'] 

print(f'Temperature: {Temperature}°C')
print(f'Humidity: {Humidity}%')