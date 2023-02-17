from aiogram import Dispatcher

from .handlers import register_NAME_handler


def register_all_handlers(dp: Dispatcher):
    register_NAME_handler(dp)
    # тут вызываете функцию с регистрацией новых хендлеров


__all__ = (
    "register_all_handlers",
)
