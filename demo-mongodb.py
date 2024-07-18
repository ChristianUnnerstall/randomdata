import randomdata
import json
from pymongo import MongoClient

# MongoDB Parameter
CONNECTION_STRING = "mongodb://192.168.178.6:27017"
DB = "database"
COLLECTION = "collection"

# Connect to MongoDB
client = MongoClient(CONNECTION_STRING)
db = client[DB]
collection = db[COLLECTION]

# Some array's
languages = ["English", "German", "Spanish"]
authors = ["John Doe", "Amy Some"]

for i in range(5):
    data = {
        "author": randomdata.EntryOfArray(authors),
        "language": randomdata.EntryOfArray(languages),
        "title": randomdata.String(50),
        "comment": randomdata.StringWithWhitespace(200),
        "meta": {
            "v": randomdata.Version(),
            "createdAt": randomdata.DateTime()
        }
    }

    print(json.dumps(data, indent=4))
    collection.insert_one(data)