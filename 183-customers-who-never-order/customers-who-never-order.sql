# Write your MySQL query statement below
SELECT name as Customers
FROM (SELECT c.id, c.name, o.customerId
FROM Customers c
LEFT JOIN Orders o 
ON c.id = o.customerId) t
WHERE customerId IS NULL
