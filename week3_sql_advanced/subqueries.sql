-- Customers who placed orders
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders
);

-- Customers who never placed orders
SELECT name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM orders
);
