import requests
import json

from tkinter import *

def get_weather(city_name):
    api_key = "f4946b41a2d6d999106aa8e914e6bdc0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def show_weather():
    city_name = city_entry.get()
    data = get_weather(city_name)

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

        output = (
            f"Temperature: {temperature_fahrenheit}°F"
            f"Pressure: {pressure} hpa"
            f"Humidity: {humidity}%"
            f"Description: {weather_description}"
            f"Wind speed: {wind_speed_mph} mph"
        )
    else: 
        output = "City not found"

    weather_output.config(text=output)

root = Tk()
root.title("Weather App")
root.geometry("600x400")


city_label = Label(root, text="Enter city name: ")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

get_weather_button = Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack()

weather_output = Label(root, text="", justify="left")
weather_output.pack()

root.mainloop()

