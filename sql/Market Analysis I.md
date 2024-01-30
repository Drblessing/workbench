```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
```

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
```

Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.

# Solution

```
SELECT u.user_id as buyer_id, u.join_date, IFNULL(o.orders_in_2019,0) AS orders_in_2019
FROM Users u
LEFT JOIN (
SELECT buyer_id, COUNT(buyer_id) as orders_in_2019
FROM Orders o
WHERE Year(order_date) = 2019
GROUP BY buyer_id) o
ON u.user_id = o.buyer_id
```

Better solutions using one query and AND statement in JOIN

```
SELECT u.user_id AS buyer_id, join_date, COUNT(order_date) AS orders_in_2019
FROM Users as u
LEFT JOIN Orders as o
ON u.user_id = o.buyer_id
AND YEAR(order_date) = '2019'
GROUP BY u.user_id
```

```
SELECT u.user_id AS buyer_id, join_date,
IFNULL(COUNT(order_date), 0) AS orders_in_2019
FROM Users as u
LEFT JOIN
Orders as o
ON u.user_id = o.buyer_id
AND YEAR(order_date) = '2019'
GROUP BY u.user_id
```
