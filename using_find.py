import pymongo
import sys

# establish connection to database

connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle on school database

db=connection.school
scores = db.scores

def find():

	print "find, reporting for duty"

	query = {'type': 'exam'}

	try:
		cursor = scores.find(query)

	except:

		print "Unexpected error", sys.exc_info()[0]

	sanity = 0
	for doc in cursor:
		print doc
		sanity += 1
		if (sanity > 10):
			break


def find_one():

	print "find one, reporting for duty"
	query = {'student_id':10}

	try:
		doc = scores.find_one(query)

	except:

		print "Unexpected error", sys.exc_info()[0]

	print doc


find()
