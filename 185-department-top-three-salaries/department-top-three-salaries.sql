# Write your MySQL query statement below
SELECT 
Department,
Employee,
Salary
FROM
(SELECT Department,Employee,Salary,
DENSE_RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) as Rank_no 
FROM
(SELECT d.name Department,e.name Employee,e.salary Salary
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id) AS emp
) AS N_emp
WHERE Rank_no <= 3;
