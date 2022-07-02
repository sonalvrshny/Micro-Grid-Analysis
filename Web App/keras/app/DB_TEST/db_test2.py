import pymongo

myclient = pymongo.MongoClient('mongodb://db:27017/')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)