
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
VAULT_TOKEN = 's.zIK1eEmJ4kSBDK1S9Oazv0oy'
VAULT_KEYNAME = 'automatik'
VAULT_KEYS = ['c7362822787993425d57f6479a65f69ee872f63e8b3df6b580d1246d3e401436fc', '90747441a715d31876423309d2f2725ef7299225efcdc57fbee761f392317d8a45', 'c54c25068774f91db72ca41531133b8d3bf004b04be16081910c34da797c4352d8', '26df763b0d1aa67b0a6c54f4bb05bb52b30f722a3047cfbeb42cd9ff2fefa9e055', '2705794cd10d32b868ce741c9cc7b1046e465fbc6be6a85f3a303903727454524f']
VAULT_ROOT_TOKEN = 's.YVGBPEcy2NSIdJyIu7x3tRz7'

# INFLUXDB
INFLUX_TOKEN = 'DAxQBKf-Y4elnhmNMyjhwQUuky2nneHeSZpWGPkqALM5k9TwgX4ZU28E4J-P7YVgj1ixmyJMhIgrPTyxAAB1nA=='



# PRODUCT DB
PRODUCT_DB_URI = 'mongodb://automatik:automatik@mongo:27017/tik_db?authSource=admin'

# MINIO
MINIO_KEY_ID = 'autoauto'
MINIO_ACCESS_KEY = 'autoauto'

SCANNER_URI = ''
SCANNER_USERNAME = ''
SCANNER_PASSWORD = ''
