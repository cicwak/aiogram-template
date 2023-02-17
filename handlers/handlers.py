from aiogram import Dispatcher

from main import dp, types


def register_NAME_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"])
    dp.register_message_handler(echo)


async def send_welcome(message: types.Message):
    await message.reply("Привет! Это шаблон для телеграм бота!")


async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
