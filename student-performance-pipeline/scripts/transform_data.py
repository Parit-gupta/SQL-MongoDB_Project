import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_pipeline"]
collection = db["student"]
data = list(collection.find())
df = pd.DataFrame(data)
print(df.head())
print("\nShape:")
print(df.shape)
print("\nMissing Values:")
print(df.isnull().sum())