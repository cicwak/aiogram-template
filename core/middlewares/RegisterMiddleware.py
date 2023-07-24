from typing import Optional

import aiogram
import sqlalchemy
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import db_session_var
from db.models.profiles import Profiles, profile_session_var


class RegisterMiddleware(LifetimeControllerMiddleware):
    """
    Simple middleware
    """

    def __init__(self):
        super(LifetimeControllerMiddleware, self).__init__()

    async def pre_process(self, obj, data, *args):
        if isinstance(obj, (
            aiogram.types.Message,
            aiogram.types.CallbackQuery
        )):
            if isinstance(obj, aiogram.types.CallbackQuery):
                obj = obj.message
            db: AsyncSession = db_session_var.get()

            if obj.chat.id < 0:
                return

            # profile: Optional[Profiles] = db.query(Profiles).filter(Profiles.tg_id == message.chat.id).first()
            profile: Optional[sqlalchemy.engine.row.Row[Profiles]] = (await db.execute(
                select(Profiles).where(Profiles.tg_id == obj.chat.id).limit(1)
            )).first()

            if profile is None:
                profile: Profiles = Profiles(
                    tg_id=obj.chat.id
                )

                db.add(profile)
                await db.commit()
                await db.refresh(profile)
            else:
                profile = profile[0]

            profile_session_var.set(profile)
