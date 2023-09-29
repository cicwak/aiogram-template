"""
Это шаблон для телеграм ботов, на базе aiogram
This is template for telegram bots, based on aiogram

дока ру https://docs.aiogram.dev/ru/latest/index.html
docs en https://docs.aiogram.dev/en/latest/index.html
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from core.config import settings
from core.redis import redis
from flows import register_handlers

API_TOKEN = settings.TG_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=RedisStorage(redis))

register_handlers(dp)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    os.system("alembic upgrade head")
    asyncio.run(main())
