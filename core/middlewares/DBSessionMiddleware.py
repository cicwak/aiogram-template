from typing import Optional

import aiogram.types
import sqlalchemy
from aiogram import types, Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware, LifetimeControllerMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import SessionLocal, db_session_var
from db.models.profiles import Profiles


class DBSessionMiddleware(LifetimeControllerMiddleware):
    """
    Simple middleware
    """
    def __init__(self):
        super(LifetimeControllerMiddleware, self).__init__()

    async def pre_process(self, obj, data, *args):
        db: AsyncSession = SessionLocal()
        db_session_var.set(db)

    async def post_process(self, obj, data, *args):
        db = db_session_var.get()
        await db.commit()
        await db.close()
