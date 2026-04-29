-- Week 2 SQL Practice (JOIN + GROUP BY)

-- Join customers and orders
SELECT 
    c.name,
    o.amount
FROM customers c
JOIN orders o
    ON c.id = o.customer_id;

-- Total orders per customer
SELECT 
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.id = o.customer_id
GROUP BY c.name;

-- Total revenue per customer
SELECT 
    c.name,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o
    ON c.id = o.customer_id
GROUP BY c.name;
