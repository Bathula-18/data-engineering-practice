-- Week 2 SQL Practice (W3Schools)

-- SELECT basics
SELECT * FROM customers;

SELECT name, city
FROM customers;

-- WHERE conditions
SELECT *
FROM customers
WHERE city = 'Chennai';

SELECT *
FROM customers
WHERE age > 25;

-- ORDER BY
SELECT *
FROM customers
ORDER BY age DESC;

-- COUNT
SELECT COUNT(*) AS total_customers
FROM customers;

-- SUM
SELECT SUM(amount) AS total_amount
FROM orders;

-- GROUP BY
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;
