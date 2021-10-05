import json
from pymongo import MongoClient, TEXT
from dotenv import load_dotenv
import os

load_dotenv()
mongo_user = os.getenv('MONGO_USERNAME')
mongo_pass = os.getenv('MONGO_PASSWORD')

client = MongoClient(f'mongodb://{mongo_user}:{mongo_pass}@localhost:27017/tik_db?authSource=admin')
db = client.tik_db
products_coll = db.products

with open('products_tik.json', mode='r') as fh:
    tik_data = fh.read()
tik_products = json.loads(tik_data.encode('utf-8'))

for p in tik_products:
    p['data-code'] = p['data-code'].rstrip('r2')
    products_coll.insert_one(p)

products_coll.create_index([('name', TEXT), ('data-code', TEXT), ('data-name', TEXT)], name='search_index', default_language='english')
client.close()

