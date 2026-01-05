from pymongo import MongoClient

MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "todo_db"

#
client = MongoClient(MONGODB_URL)
database = client[DATABASE_NAME]
collection = database["todos"]
