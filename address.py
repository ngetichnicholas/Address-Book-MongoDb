import pymongo
from pymongo import MongoClient
from decouple import config

cluster = MongoClient(f"mongodb+srv://NgetichNick:{config('PASS')}@cluster0.0gaxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["address"]
collection = db["address"]
# post = {"_id": 0, "name": "Nick", "address": "Berlin 63"}


# results = collection.find({"name":"Nick"})
# results = collection.delete_one({"name":"Nick"})
results = collection.update_one({"name":"Nick"},{"$set":{"name":"Nicholas"}})
# results = collection.delete_many({})



# for result in results:
#     print(result)

# collection.insert_one(post)