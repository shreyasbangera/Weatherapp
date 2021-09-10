from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = 'config.ini'
config = ConfigParser()
config.read(api_file)
api_key = config['api']['key']


def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country = json_file['sys']['country']
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature - 273.15
        weather_display = json_file['weather'][0]['main']
        result = [city, country, c_temperature, weather_display]

        return result
    else:
        return None


def print_weather():
    city = search_city.get()
    wthr = weather_find(city)
    if weather:
        location_entry['text'] = '{},{}'.format(wthr[0], wthr[1])
        temperature_entry['text'] = '{:.2f} C'.format(wthr[2], wthr[3])
        wthr_entry['text'] = wthr[3]
    else:
        messagebox.showerror('Error', 'Please enter a valid city name')


weather = Tk()
weather.title("Weather app")
weather.config(bg="white")
weather.geometry("700x400")
search_city = StringVar()
enter_city = Entry(weather, textvariable=search_city, fg="black", font=("Calibre", 25))
enter_city.pack()
search_button = Button(weather, text='SEARCH', width=10, bg="blue", fg="white", font=("calibre", 15),
                       command=print_weather)
search_button.pack()
location_entry = Label(weather, text='', font=("Calibre", 25))
location_entry.pack()
temperature_entry = Label(weather, text='', font=("Calibre", 25))
temperature_entry.pack()
wthr_entry = Label(weather, text='', font=("Calibre", 25))
wthr_entry.pack()

weather.mainloop()
