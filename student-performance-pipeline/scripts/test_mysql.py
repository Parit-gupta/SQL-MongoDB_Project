import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@202317Abc"
)
print("Connected successfully")
conn.close()