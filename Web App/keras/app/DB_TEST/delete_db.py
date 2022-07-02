import pymongo

db_client = pymongo.MongoClient('mongodb://db:27017/')
mydb = db_client["mydatabase"]
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")