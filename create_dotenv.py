import hvac

def init_vault():
    # INIT
    client = hvac.Client(url='http://localhost:8200')
    # ic(client.is_authenticated())
    # ic(client.sys.is_initialized())
    shares = 5
    threshold = 3
    #
    result = client.sys.initialize(shares, threshold)
    print(result['root_token'])
    print(result['keys'])

    with open(".env", "w") as f:
        f.write(f"VAULT_ROOT_TOKEN={result['root_token']}")
        f.write(f"VAULT_KEYS={result['keys']}")
    

def main():
    import os
    import sys

    if os.path.exists(".env"):
        print(".env file already exists. Exiting...")
        sys.exit()

    init_vault()

if __name__ == "__main__":
    main()
    



