
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str  # autmatically taken from environement variable
    token_url: str = "/api/auth/login"

    mongo_host: str = "mongodb"
    mongo_user: str = "sekuritim"
    mongo_pass: str = "sekuritim"
    mongo_db: str = "automatik"

    @property
    def mongo_dsn(self):
        return f"mongodb://automatik:automatik@mongodb:27017/automatik?authSource=admin"


DEFAULT_SETTINGS = Settings(_env_file=".env")

# MONGO CONFIG
# import os

DB_URI = 'mongodb://automatik:automatik@mongodb:27017/automatik?authSource=admin'

# VAULT CONFIG
VAULT_URL = 'http://vault:8200'
VAULT_TOKEN = 'vault_token'
VAULT_KEYNAME = 'automatik'
VAULT_KEYS = ['asdasd', 'asdasdsa']

# INFLUXDB
INFLUX_TOKEN = 'asdoija9083ud2=='



# PRODUCT DB
PRODUCT_DB_URI = 'mongodb://automatik:automatik@mongodb:27017/tik_db?authSource=admin'

# MINIO
MINIO_KEY_ID = 'autokaka'
MINIO_ACCESS_KEY = 'autokaka'
