from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PSQL_DB_")

    database: str
    username: str
    password: str
    host: str
    port: str


postgres_settings = PostgresSettings()

class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")

    host: str = "redis-cache"
    port: int = 6379
    token_expiration_seconds: int = 3600


redis_settings = RedisSettings()

DATABASE_URL = "postgres://{}:{}@{}:{}/{}".format(
    postgres_settings.username,
    postgres_settings.password,
    postgres_settings.host,
    postgres_settings.port,
    postgres_settings.database,
)

models = ["app.authentication.models", "aerich.models"]
