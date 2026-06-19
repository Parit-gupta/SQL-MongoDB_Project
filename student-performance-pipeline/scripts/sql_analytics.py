import pandas as pd
import mysql.connector
import os

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@202317Abc",
    database="student_analytics"
)

os.makedirs("results", exist_ok=True)

queries = {
    "Top 10 Students": """
        SELECT student_id,
               average_score
        FROM student_scores
        ORDER BY average_score DESC
        LIMIT 10
    """,

    "Average Score by Gender": """
        SELECT gender,
               ROUND(AVG(average_score),2) AS avg_score
        FROM student_scores
        GROUP BY gender
    """,

    "Average Score by School Type": """
        SELECT school_type,
               ROUND(AVG(average_score),2) AS avg_score
        FROM student_scores
        GROUP BY school_type
    """,

    "Attendance vs Performance": """
        SELECT attendance_category,
               ROUND(AVG(average_score),2) AS avg_score
        FROM student_scores
        GROUP BY attendance_category
        ORDER BY avg_score DESC
    """,

    "Grade Distribution": """
        SELECT final_grade,
               COUNT(*) AS total_students
        FROM student_scores
        GROUP BY final_grade
        ORDER BY total_students DESC
    """,

    "Top 10 Ranked Students": """
        SELECT student_id,
               average_score,
               RANK() OVER(
                   ORDER BY average_score DESC
               ) AS student_rank
        FROM student_scores
        LIMIT 10
    """
}

for title, query in queries.items():

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    df = pd.read_sql(query, conn)

    print(df)

    filename = title.lower().replace(" ", "_") + ".csv"

    df.to_csv(
        f"results/{filename}",
        index=False
    )

    print(f"\nSaved {filename}")

conn.close()

print("\nAll analytics reports generated successfully.")