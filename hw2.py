import pymongo

from pymongo import MongoClient

# connect to database

connection = MongoClient('localhost', 27017)

db = connection.test

# handle to grades collection
#grades = db.grades

cur = db.grades.find()

cur.next()