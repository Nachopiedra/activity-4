from app.authentication.persistence.redis.token import RedisTokenPersistence
from app.config import redis_settings

token_persistence = RedisTokenPersistence(
    host=redis_settings.host,
    port=redis_settings.port,
    expiration_seconds=redis_settings.token_expiration_seconds,
)
