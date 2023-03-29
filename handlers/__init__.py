from aiogram import Dispatcher

from .commands import start
from .messages import echo


def register_all_handlers(dp: Dispatcher):
    # commands
    dp.register_message_handler(start, commands=["start"])

    # messages
    dp.register_message_handler(echo)

    # тут вызываете функцию с регистрацией новых хендлеров


__all__ = (
    "register_all_handlers",
)
