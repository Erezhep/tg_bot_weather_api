from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import requests
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API = os.getenv('WEATHER_API')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"

def get_info(
        url: str, 
        api_key: str, 
        city: str, 
        units: str = "metric", 
        lang: str = "ru"
    ) -> str:
    
    r = requests.get(url = url, 
                     params = {
                        "q": city, 
                        "APPID": api_key, 
                        'units': units, 
                        "lang": lang
                                }
                    )
    if r.status_code == 200:
        data = r.json()
        name_city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return (f"Погода в городе {name_city}\nТемпература: {temp}\nВлажность: {humidity}\nОписание: {description}")
    return "Город не найден или API запрос не удался"
    
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
def send_start(message: types.Message):
    username = message.from_user.first_name
    return message.answer(f"Привет, {username}! Я помогу вам узнать погоду в любом городе. Просто отправьте название города, и я предоставлю актуальную информацию!")

@dp.message()
def info_weather(message: types.Message):
    text = get_info(url = BASE_URL, 
                    api_key = WEATHER_API,
                    city = message.text)
    return message.answer(text)


if __name__ == "__main__":
    dp.run_polling(bot)