import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_pipeline"]
collection = db["student"]
data = list(collection.find())
df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)
df["average_score"] = (
    df["math_score"] +
    df["science_score"] +
    df["english_score"]
) / 3
df["attendance_category"] = pd.cut(
    df["attendance_percentage"],
    bins=[0, 60, 75, 90, 100],
    labels=["Low", "Medium", "High", "Excellent"]
)
print(df.head())
print("\nDuplicates Removed:")
print(df.duplicated().sum())
print("\nAverage Score Created")
print("\nAttendance Categories:")
print(df["attendance_category"].value_counts())
