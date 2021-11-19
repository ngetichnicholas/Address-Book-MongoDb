import pymongo
from pymongo import MongoClient
from decouple import config

cluster = MongoClient(f"mongodb+srv://NgetichNick:{config('PASS')}@cluster0.0gaxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["address"]
collection = db["address"]
post = [
    {"_id": 1, "name": "Ben", "address": "Berlin 63"},
    {"_id": 2, "name": "Mark", "address": "Nairobi 46"}
]

# results = collection.find({"name":"Nick"})
results = collection.delete_one({"name":"Nick"})
# results = collection.delete_many({})



# for result in results:
#     print(result)

collection.insert_many(post)