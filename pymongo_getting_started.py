import pymongo

from pymongo install MongoCLient

# connect to database

connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']