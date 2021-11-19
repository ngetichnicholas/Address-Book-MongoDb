from pymongo import MongoClient
addressclient = MongoClient()
myclient = MongoClient('localhost',27017)
address_book = myclient["address"]
address_collection = address_book["addresscollection"]

collection_list = [
    {"id": 1, "name": "John", "address": "Abuja 47"},
    {"id": 2, "name": "Mark", "address": "Kampala 37"},
    {"id": 3, "name": "Nick", "address": "Chicago 65"},
    {"id": 4, "name": "Ben", "address": "Nairobi 42"},
    {"id": 5, "name": "Jane", "address": "Berlin 12"},
    {"id": 6, "name": "Ken", "address": "Tokyo 34"},
    {"id": 7, "name": "Timo", "address": "Paris 17"},
    {"id": 8, "name": "Luke", "address": "Lagos 25"},
    {"id": 9, "name": "Caleb", "address": "London 47"},

]

address_collection.insert_many(collection_list)
dblist = myclient.list_database_names()
 
print(dblist)