Table: Weather

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature on a certain day.
```

Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

# Solution

LAG

```
SELECT DISTINCT(w.id)
FROM (SELECT *,
LAG(recordDate,1) OVER (ORDER BY recordDate)  as prevDate,
LAG(temperature,1) OVER (ORDER BY recordDate) as prevTemp
FROM Weather) w
WHERE w.temperature > w.prevTemp
AND DATEDIFF(w.recordDate,w.prevDate) = 1
```

DOUBLE INNER JOIN

```
SELECT DISTINCT(w1.id)
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature
AND DATEDIFF(w1.recordDate,w2.recordDate) = 1
```
