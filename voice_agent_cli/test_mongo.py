from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["voice_agent"]
collection = db["test"]
collection.insert_one({"message":"succesfully connected"})
print("MongoDb working")