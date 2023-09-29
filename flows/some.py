from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def some(message: Message):
    await message.answer("А это ты уже чет не то ввел мудила")
