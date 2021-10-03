
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str  # autmatically taken from environement variable
    token_url: str = "/api/auth/login"

    mongo_host: str = "mongo"
    mongo_user: str = "automatik"
    mongo_pass: str = "automatik"
    mongo_db: str = "automatik"

    @property
    def mongo_dsn(self):
        return f"mongodb://automatik:automatik@mongo:27017/automatik?authSource=admin"


DEFAULT_SETTINGS = Settings(_env_file=".env")

# MONGO CONFIG
# import os

DB_URI = 'mongodb://automatik:automatik@mongo:27017/automatik?authSource=admin'

# VAULT CONFIG
VAULT_URL = 'http://vault:8200'
VAULT_TOKEN = 's.simmRq1ikXCHrYWiUXyO0NcI'
VAULT_KEYNAME = 'automatik'
VAULT_KEYS = ['d98a842ac43bd013fbc1e302a3b4dd7ce15609bfcbf1a432bedc590889a7c666f8', 'fc7c0ef4a64981a5d24fd346e4c0f276b535e669f57ce63896a474e335ac8ba9b6', '5a366f5473efa57ec8fbf2998ca8e813dc16ac1fdc55575e7243b9784977dae9e9', '96b49d290207bee0e95bd9e711a97fbb46ff00641ad8d4d5ca8a010bac4e69fc46', 'cb831ab1d9e7f12cc6e6b6e91d58a8397d1c2771846e540b66e27cc660e04ef61e']
VAULT_ROOT_TOKEN = 's.GgNi33iTCMbdGRkMUua7582o'

# INFLUXDB
INFLUX_TOKEN = '6hAQusSTSzGHXc5IYvZ99KhrGtOMhOGEOkwZjdDzZaytIlRFAMVtwLzz2FkRPzsELiz_nco9O1Q6OQvhnY4bvQ=='



# PRODUCT DB
PRODUCT_DB_URI = 'mongodb://automatik:automatik@mongo:27017/tik_db?authSource=admin'

# MINIO
MINIO_KEY_ID = 'auto_user'
MINIO_ACCESS_KEY = 'auto_user'

SCANNER_URI = ''
SCANNER_USERNAME = ''
SCANNER_PASSWORD = ''
