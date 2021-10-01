import hvac
from rich.console import Console
import os
import sys
    

def init_vault():
    # INIT
    client = hvac.Client(url='http://localhost:8200')
    shares = 5
    threshold = 3
    
    result = client.sys.initialize(shares, threshold)

    return result['token'], result['keys']

    

def main():
    console = Console(color_system="auto")
    # with console.status("Working...", spinner="dots"):
    # if os.path.exists(".env"):
    #     console.print("[red].env file already exists. Exiting...")
    #     sys.exit()
    token, keys = init_vault()

    mongo_user = console.input("[green]MongoDB Username: ")
    mongo_pass = console.input("[green]MongoDB Password: ")

    minio_user = console.input("[green]Minio Username: ")
    minio_pass = console.input("[green]Minio Password: ")

    # influx_token = console.input("[green]InfluxDB Token: ")
    
    # init_vault()
    # console.print('[green]Vault initialized...')

    with open(".env", "w") as f:
        f.write(f"VAULT_ROOT_TOKEN={token}\n")
        f.write(f"VAULT_KEYS={keys}\n")
        f.write("\n")
        f.write(f"MONGO_USERNAME={mongo_user}\n")
        f.write(f"MONGO_PASSWORD={mongo_pass}\n")
        f.write("\n")
        f.write(f"MINIO_USERNAME={minio_user}\n")
        f.write(f"MINIO_PASSWORD={minio_pass}\n")
        f.write("\n")
        

if __name__ == "__main__":
    main()
    



