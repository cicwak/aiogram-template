"""
Это шаблон для телеграм ботов, на базе aiogram
This is template for telegram bots, based on aiogram

дока ру https://docs.aiogram.dev/ru/latest/index.html
docs en https://docs.aiogram.dev/en/latest/index.html
"""

import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from handlers import register_all_handlers


API_TOKEN = os.getenv("TG_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_all_handlers(dp)  # регистрация хендлеров!


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
