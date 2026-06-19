# MongoDB Notes

## Database Information

Database Name:
student_pipeline

Collection Name:
student

## Purpose

MongoDB is used as the raw data storage layer in this project.

The original CSV dataset is first ingested into MongoDB before being transformed and loaded into MySQL for analytical processing.

## Collection Statistics

Records Inserted:
25,000

## Sample Document Structure

{
"student_id": 1,
"age": 14,
"gender": "male",
"school_type": "public",
"parent_education": "post graduate",
"study_hours": 3.1,
"attendance_percentage": 84.3,
"internet_access": "yes",
"travel_time": "<15 min",
"extra_activities": "yes",
"study_method": "notes",
"math_score": 42.7,
"science_score": 55.4,
"english_score": 57.0,
"overall_score": 53.1,
"final_grade": "E"
}

## MongoDB Operations Used

- insert_many()
- find()
- find_one()
- count_documents()

## Verification Commands

show dbs

use student_pipeline

show collections

db.student.countDocuments()

db.student.findOne()
