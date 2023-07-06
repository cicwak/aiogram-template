from aiogram import Dispatcher

from core.middlewares.DBSessionMiddleware import DBSessionMiddleware
from core.middlewares.RegisterMiddleware import RegisterMiddleware


def register_middleware(dp: Dispatcher):
    dp.setup_middleware(DBSessionMiddleware())
    dp.setup_middleware(RegisterMiddleware())


__all__ = (
    "register_middleware",
)
