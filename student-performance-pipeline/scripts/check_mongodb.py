from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["student_pipeline"]
collection = db["student"]
print("Total Records:")
print(collection.count_documents({}))
print("\nFirst Record:")
print(collection.find_one())