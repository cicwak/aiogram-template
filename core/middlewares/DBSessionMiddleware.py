from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import SessionLocal, db_session_var


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
