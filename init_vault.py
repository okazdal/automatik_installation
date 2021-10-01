import hvac

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

with open('VAULT_ROOT_TOKEN', mode='w') as fh:
    fh.write(result['root_token'])