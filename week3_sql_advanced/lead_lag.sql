-- LAG
SELECT 
    customer_id,
    order_date,
    amount,
    LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_amount
FROM orders;

-- LEAD
SELECT 
    customer_id,
    order_date,
    amount,
    LEAD(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_amount
FROM orders;
