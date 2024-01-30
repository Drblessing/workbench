Table: Orders

```
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key for this table.
This table contains information about the order ID and the customer ID.
```

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

# Solution

```
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
```

Having

```
SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
	SELECT COUNT(order_number) cnt
	FROM orders
	GROUP BY customer_number
	ORDER BY cnt DESC
	LIMIT 1
)
```

Window function, handles multiple customers with same number of order

```
select customer_number
from (select customer_number, DENSE_RANK() over (order by count desc) as 'ranking'
      from (select customer_number, count(customer_number) as count from orders group by customer_number)sub1
      ) sub2
where sub2.ranking = 1;
```

All customers with higest order

```
select customer_number
from orders
group by customer_number
having count(order_number) = (select count(*) as count
                              from orders
                              group by customer_number
                              order by count desc limit 1);
```
