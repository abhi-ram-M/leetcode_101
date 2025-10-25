# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees as em
LEFT JOIN EMployeeUNI as uni
ON em.id = uni.id