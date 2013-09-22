import pymongo
import sys

# establish connection to database

connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle on school database

db=connection.students
grades = db.grades

def find():

	print "find, lowest homework by student"

	# Hint/spoiler: If you select homework grade-documents
	# sort by student and then by score, you can iterate through 
	# and find the lowest score for each student by noticing a change in student id. 
	# As you notice that change of student_id, remove the document.

	query = {'type': 'homework'}

	try:
		cursor = grades.find(query)
		cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
	except:

		print "Unexpected error", sys.exc_info()[0]

	sanity = 0
	for doc in cursor:
		print doc
		sanity += 1
		if (sanity > 10):
			break

find()