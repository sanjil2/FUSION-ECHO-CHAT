import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db_name = 'groot'
collection_name = 'groot_intents'

if db_name in client.list_database_names():
    db = client[db_name]
else:
    db = client[db_name]
    collection = db[collection_name]
    # Read intents.json file
    with open('_intents.json') as file:
        intents_data = json.load(file)
    # Insert data into MongoDB
    collection.insert_many(intents_data['intents'])
