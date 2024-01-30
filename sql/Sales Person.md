Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

# Solution

```
SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN
(SELECT DISTINCT(o.sales_id)
FROM Orders o
LEFT JOIN Company c
USING(com_id)
WHERE c.name = "RED")
```

Double Join

```
select salesperson.name
from orders o join company c on (o.com_id = c.com_id and c.name = 'RED')
right join salesperson on salesperson.sales_id = o.sales_id
where o.sales_id is null
```
