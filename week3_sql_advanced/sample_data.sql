-- Customers table
CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INT,
    updated_at DATE
);

-- Orders table
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount INT,
    status VARCHAR(20)
);
