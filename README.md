# Student Performance Data Pipeline

## Project Overview

This project demonstrates an end-to-end Data Engineering pipeline using MongoDB, Pandas, and MySQL.

Raw student performance data is ingested from a CSV dataset, stored in MongoDB, transformed using Pandas, loaded into MySQL, and analyzed using SQL queries.

---

## Architecture

Student_Performance.csv

↓

MongoDB (Raw Data Storage)

↓

Pandas (Data Transformation)

↓

MySQL (Analytics Database)

↓

SQL Reports & Insights

---

## Dataset Information

Dataset: Student Performance Dataset

Total Records: 25,000

Features:

- Student Demographics
- School Information
- Study Habits
- Attendance Percentage
- Subject Scores
- Final Grades

---

## Technologies Used

- Python
- Pandas
- MongoDB
- MySQL
- SQLAlchemy
- MySQL Connector
- SQL

---

## ETL Pipeline

### Extract

- Read dataset from CSV file.
- Convert records into MongoDB documents.

### Transform

- Remove duplicate records.
- Create average_score feature.
- Create attendance_category feature.
- Perform data quality validation.

### Load

- Store raw data in MongoDB.
- Load transformed data into MySQL.

---

## Project Structure

student-performance-pipeline/

├── data/

├── mongodb/

├── results/

├── scripts/

├── sql/

├── README.md

└── requirements.txt

---

## Scripts

### load_to_mongodb.py

Loads CSV data into MongoDB.

### check_mongodb.py

Verifies MongoDB insertion and collection statistics.

### transform_data.py

Transforms MongoDB data using Pandas.

### load_to_sql.py

Loads transformed data into MySQL.

### sql_analytics.py

Runs SQL analytics and exports reports.

---

## SQL Analytics Performed

### Top 10 Students

Identifies highest-performing students based on average score.

### Average Score by Gender

Compares academic performance across genders.

### Average Score by School Type

Compares public and private school performance.

### Attendance vs Performance

Analyzes relationship between attendance and academic outcomes.

### Grade Distribution

Calculates distribution of final grades.

### Student Ranking

Ranks students using SQL Window Functions.

---

## Generated Reports

Reports are automatically generated inside the results folder.

Examples:

- top_10_students.csv
- average_score_by_gender.csv
- average_score_by_school_type.csv
- attendance_vs_performance.csv
- grade_distribution.csv
- top_10_ranked_students.csv

---

## Key Learnings

- MongoDB document storage
- Data transformation using Pandas
- ETL pipeline concepts
- SQL analytics and reporting
- Database integration using Python
- Window Functions in SQL
- Automated report generation

---

## Future Improvements

- Apache Airflow integration
- PostgreSQL support
- Power BI dashboard
- Streamlit analytics dashboard
- Data warehouse implementation

---

## Resume Highlights

- Built a Data Engineering pipeline processing 25,000 student records.
- Implemented MongoDB-based raw data storage layer.
- Performed data transformation using Pandas.
- Loaded processed data into MySQL for analytical reporting.
- Developed SQL analytics using joins, aggregations, and window functions.
- Automated report generation and export using Python.
