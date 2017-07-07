import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017) #connect to the mongo instance running on the system

db = client['psosm']	#connect to the required data base
collection = db['presenters']		#connect to the required collection


#Querying documents from a collection

for item in collection.find():
	print item
	print

# exit()

#Let's create a new collection

detailed_collection = db['participant_details']
"""
p1 = { "name" : "Divyansh", "age" : 22, "affiliation" : "NSIT" , "interests" : ["Programming","Movies", "Reading"] }
p2 = { "name" : "Kushagra", "age" : 23, "affiliation" : "BVP" , "interests" : ["Programming","Dance", "Reading"] }
p3 = { "name" : "Anupama", "age" : 21, "affiliation" : "IIIT-D" , "interests" : ["Programming","Food", "Reading"] }
p4 = { "name" : "Neha", "age" : 20, "affiliation" : "BITS - Pilani" , "interests" : ["Music","Movies", "Programming"] }

#Insert data into the collection

detailed_collection.insert(p1)
detailed_collection.insert(p2)
detailed_collection.insert(p3)
detailed_collection.insert(p4)
"""
#To insert an array(list) of jsons, use insert_many command


#To get one document from the collection

print detailed_collection.find_one()


#To get all documents from the collection
"""
for item in detailed_collection.find():
	print item
	print
"""


#To prettify the printing of the mongo documents, we use a package called pretty print

import pprint

pprint.pprint(detailed_collection.find_one())


#Conditional querying

for person in detailed_collection.find({"name" : "Divyansh"}):
	print person


#Update the document in a collection :-

detailed_collection.update({"name" : "Divyansh"},{"$set": {"name" : "Divyansh Agarwal"}}, upsert = True)
