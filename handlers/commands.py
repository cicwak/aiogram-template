from aiogram import types


async def start(message: types.Message):
    await message.reply("Привет! Это шаблон для телеграм бота!")
