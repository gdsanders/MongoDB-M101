import bottle

import pymongo

# this is the handler for the default path of web server

@bottle.route('/')
def index():

	# connect to MongoDB

	connection = pymongo.MongoClient('localhost', 27017)

	# attach to test database

	db = connection.test

	# get handle for names

	name = db.names

	# find a single document

	item = name.find_one()

	return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)