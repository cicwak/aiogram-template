from redis.asyncio import from_url

from core.config import settings

redis = from_url(settings.REDIS_URL)
