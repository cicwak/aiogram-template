from core.config import settings
from redis.asyncio import from_url

redis = from_url(settings.REDIS_URL)
