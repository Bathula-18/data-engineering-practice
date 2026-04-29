-- CTE example

WITH filtered_customers AS (
    SELECT customer_id, name, age
    FROM customers
    WHERE age > 25
)
SELECT *
FROM filtered_customers;
