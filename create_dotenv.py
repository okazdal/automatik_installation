import hvac
from rich.console import Console
import os
import sys
    

def main():
    console = Console(color_system="auto")
    # with console.status("Working...", spinner="dots"):
    if os.path.exists(".env"):
        console.print("[red].env file already exists. Please delete it. Exiting...")
        sys.exit()

    mongo_user = console.input("[green]MongoDB Username: ")
    mongo_pass = console.input("[green]MongoDB Password: ")

    minio_user = console.input("[green]Minio Root Username: ")
    minio_pass = console.input("[green]Minio Root Password: ")

    with open(".env", "w") as f:
        f.write(f"SECRET={os.urandom(24).hex()}")
        f.write("\n")
        f.write(f"MONGO_USERNAME={mongo_user}\n")
        f.write(f"MONGO_PASSWORD={mongo_pass}\n")
        f.write("\n")
        f.write(f"MINIO_USERNAME={minio_user}\n")
        f.write(f"MINIO_PASSWORD={minio_pass}\n")
        f.write("\n")
        

if __name__ == "__main__":
    main()
    



