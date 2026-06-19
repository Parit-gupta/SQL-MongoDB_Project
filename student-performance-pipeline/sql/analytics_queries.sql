SELECT gender,
ROUND(AVG(average_score),2) AS avg_score
FROM student_scores
GROUP BY gender;

SELECT school_type,
ROUND(AVG(average_score),2) AS avg_score
FROM student_scores
GROUP BY school_type;

SELECT student_id,
average_score,
RANK() OVER(
    ORDER BY average_score DESC
) AS student_rank
FROM student_scores;