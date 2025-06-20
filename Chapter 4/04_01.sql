USE etl_course_db;

SELECT * FROM customers
LIMIT 100;

SELECT COUNT(*)
FROM customers
WHERE State='TX';

SELECT COUNT(*)
FROM customers
WHERE State='TX' and City='Dallas';

SELECT State, City, COUNT(CustomerID) AS CustomerCount
FROM Customers
GROUP BY State, City
ORDER BY CustomerCount DESC;

SELECT * FROM orders;
SELECT * FROM products;