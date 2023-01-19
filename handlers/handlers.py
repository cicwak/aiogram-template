from main import dp, types


@dp.message_handler(commands=['start', 'help'], )
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это шаблон для телеграм бота!")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
