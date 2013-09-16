import pymongo

def main():

	connection = pymongo.MongoClient("mongodb://localhost")

	db = connection.m101
	people = db.people

	person = {'name':'Benjamin Franklin', 'role':'President',
		'address':{'address1':'The White House', 'address2':'1600 Pennsylvania Avenue', 
		'city':'Washington'}, 'interests':['writing','kite flying','French women']}

	people.insert(person)

main()