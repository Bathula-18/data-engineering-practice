-- ROW_NUMBER
SELECT 
    customer_id,
    amount,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rn
FROM orders;

-- RANK
SELECT 
    amount,
    RANK() OVER (ORDER BY amount DESC) AS rnk
FROM orders;

-- DENSE_RANK
SELECT 
    amount,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS drnk
FROM orders;
