from aiogram import Dispatcher
from flows.some import router as some_router
from flows.start import router as start_router


def register_handlers(dp: Dispatcher):
    dp.include_routers(
        start_router,
        some_router
    )
