# Parser for weather
from telegram import Update
from telegram.ext import ContextTypes
import requests
from credits import API_key


def find_wind_direction(degree):
    if degree in range(348, 361) or degree in range(0, 12):
        return 'северный'
    elif degree in range(12, 78):
        return 'северо-восточный'
    elif degree in range(78, 101):
        return 'западный'
    elif degree in range(101, 168):
        return 'юго-восточный'
    elif degree in range(168, 191):
        return 'южный'
    elif degree in range(191, 258):
        return 'юго-западный'
    elif degree in range(258, 281):
        return 'западный'
    elif degree in range(281, 348):
        return 'северо-западный'


async def show_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city_name = 'Чебоксары'
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={API_key}"
    )
    data = response.json()

    # Extracting data
    weather = data['weather'][0]['description']
    if 'снег' in weather:
        weather = f'идет {weather}'

    wind_direction = find_wind_direction(data['wind']['deg'])
    wind_speed = round(data['wind']['speed'])
    pressure = round(data['main']['pressure'] * 0.7501)
    temperature = round(data['main']['temp'])
    humidity = data['main']['humidity']

    report = f'По данным сервиса OpenWeather на данный час в г.{city_name} {weather}.\n' \
             f'Температура воздуха {temperature} градусов Цельсия.\n' \
             f'Относительная влажность воздуха {humidity} %.\n' \
             f'Атмосферное давление {pressure} мм рт.ст.\n' \
             f'Ветер {wind_direction}, {wind_speed} м/с.'

    await context.bot.send_message(update.effective_chat.id,
                                   text=f"{report}")
