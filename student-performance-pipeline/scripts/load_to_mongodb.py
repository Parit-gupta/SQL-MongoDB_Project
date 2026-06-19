import pandas as pd
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["student_pipeline"]
collection = db["student"]
df = pd.read_csv("data/Student_Performance.csv")
records = df.to_dict("records")
collection.insert_many(records)
print(f"{len(records)} records inserted successfully")