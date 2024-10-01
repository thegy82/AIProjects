import requests
import json

api_key = "f4946b41a2d6d999106aa8e914e6bdc0"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
data = response.json()

if data["cod"] != "404":
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]

    temperature = main["temp"]

    # convert temp from kelvin to fahrenheit
    temperature_fahrenheit = round((temperature - 273.15) * 9/5 + 32)
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_description = weather["description"]
    wind_speed = wind["speed"]

    # convert wind speed from mps to mph
    wind_speed_mph = wind_speed * 2.237

    print(f"Temperature: {temperature_fahrenheit}°F")
    print(f"Pressure: {pressure} hpa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
    print(f"Wind speed: {wind_speed_mph} mph")
else: 
    print("City not found")

