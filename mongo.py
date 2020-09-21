import pymongo
import os

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "MilestoneProjectThree"
COLLECTION_NAME = "Recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'recipe_name':'chocolate black bean muffins','yield':'Makes 12 muffins','equipment':'blender, measuring cups and spoons, muffin tin, cooking oil spray, rubber spatula, cooling rack'}

coll.insert_one(new_doc)

documents = coll.find()

for doc in documents: 
    print(doc)
