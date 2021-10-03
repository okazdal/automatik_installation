import hvac
from rich.console import Console
from dotenv import load_dotenv
import os
import sys
    

def init_vault():
    # INIT
    client = hvac.Client(url='http://localhost:8200')
    shares = 5
    threshold = 3
    
    result = client.sys.initialize(shares, threshold)

    return result['root_token'], result['keys']


def unseal(keys):
    client = hvac.Client(url='http://localhost:8200')
    client.sys.submit_unseal_keys(keys)

def create_policy(root_token):
    client = hvac.Client(url='http://localhost:8200')
    client.token = root_token
    policy = '''
        path "kv/data/automatik/*" {
        capabilities = ["create", "read", "update", "delete"]
        }

        path "transit/*" {
        capabilities = ["create", "read", "update", "delete"]
        }

        path "auth/token/renew" {
        capabilities = ["update"]
        }
    '''
    client.sys.create_or_update_policy(
        name='automatik',
        policy=policy,
    )

def create_token(root_token):
    client = hvac.Client(url='http://localhost:8200')
    client.token = root_token

    token = client.auth.token.create(policies=['automatik'])
    return token['auth']['client_token']

def main():
    console = Console(color_system="auto")
    # with console.status("Working...", spinner="dots"):

    load_dotenv()
    mongo_user = os.getenv('MONGO_USERNAME')
    mongo_pass = os.getenv('MONGO_PASSWORD')
    
    
    vault_root_token, vault_keys = init_vault()
    
    console.print('[green]Vault initialized...')
    # UNSEAL
    unseal(vault_keys)
    # CREATE POLICY
    create_policy(vault_root_token)
    # CREATE TOKEN
    vault_token = create_token(vault_root_token)

    influx_token = console.input("[green]InfluxDB Token: ")
    minio_username = console.input("[green]Minio Username: ")
    minio_password = console.input("[green]Minio Password: ")
    

    CONFIG = f'''
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str  # autmatically taken from environement variable
    token_url: str = "/api/auth/login"

    mongo_host: str = "mongo"
    mongo_user: str = "{mongo_user}"
    mongo_pass: str = "{mongo_pass}"
    mongo_db: str = "automatik"

    @property
    def mongo_dsn(self):
        return f"mongodb://{mongo_user}:{mongo_pass}@mongo:27017/automatik?authSource=admin"


DEFAULT_SETTINGS = Settings(_env_file=".env")

# MONGO CONFIG
# import os

DB_URI = 'mongodb://{mongo_user}:{mongo_pass}@mongo:27017/automatik?authSource=admin'

# VAULT CONFIG
VAULT_URL = 'http://vault:8200'
VAULT_TOKEN = '{vault_token}'
VAULT_KEYNAME = 'automatik'
VAULT_KEYS = {vault_keys}
VAULT_ROOT_TOKEN = '{vault_root_token}'

# INFLUXDB
INFLUX_TOKEN = '{influx_token}'



# PRODUCT DB
PRODUCT_DB_URI = 'mongodb://{mongo_user}:{mongo_pass}@mongo:27017/tik_db?authSource=admin'

# MINIO
MINIO_KEY_ID = '{minio_username}'
MINIO_ACCESS_KEY = '{minio_password}'

SCANNER_URI = ''
SCANNER_USERNAME = ''
SCANNER_PASSWORD = ''
'''

    with open("config/config.py", "w") as f:
        f.write(CONFIG)
    console.print('[green]CONFIG file written to config/config.py')

if __name__ == "__main__":
    main()
    



