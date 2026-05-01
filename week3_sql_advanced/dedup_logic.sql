-- Deduplication: Keep latest record per transanction using ROW_NUMBER
-- Latest record per customer

SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM customers
) t
WHERE rn = 1;
