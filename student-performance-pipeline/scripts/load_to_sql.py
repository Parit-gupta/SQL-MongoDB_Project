import pandas as pd
from pymongo import MongoClient
from sqlalchemy import create_engine

client = MongoClient("mongodb://localhost:27017/")
db = client["student_pipeline"]

data = list(db["student"].find())

df = pd.DataFrame(data)

df.drop(columns=["_id"], inplace=True)

df["average_score"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
) / 3

df["attendance_category"] = pd.cut(
    df["attendance_percentage"],
    bins=[0, 60, 75, 90, 100],
    labels=["Low", "Medium", "High", "Excellent"]
)

engine = create_engine(
    "mysql+mysqlconnector://root:%40202317Abc@localhost/student_analytics"
)

df.to_sql(
    "student_scores",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")