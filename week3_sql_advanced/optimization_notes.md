# Query Optimization, Indexes and Execution Plan

## Query Optimization

Query optimization means writing SQL in a way that reduces unnecessary work for the database.

Main points:
- Select only required columns
- Use WHERE clause to filter early
- Avoid unnecessary joins

## Index

An index helps the database locate required rows faster.

Example:
If the orders table has an index on order_date, filtering by order_date can be faster.

```sql
CREATE INDEX idx_order_date
ON orders(order_date);

## Execution Plan

Execution plan shows how the database runs a query.

It helps to:
- check if index is used
- check if full table scan is happening
- identify slow parts of query
