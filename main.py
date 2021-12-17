import requests
from bs4 import BeautifulSoup
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def get_fact():
    r = requests.get('https://randstuff.ru/fact/')
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    sel = soup.select("#" + 'fact')
    return sel[0].get_text()[:sel[0].get_text().rfind('.')]


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, пришлю рандомный факт")


@dp.message_handler()
async def process_start_command(message: types.Message):
    s = get_fact()
    # noinspection PyTypeChecker
    await bot.send_message(message.from_user.id, s)


if __name__ == '__main__':
    executor.start_polling(dp)