# Big Countries

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |
+-------------+---------+
name is the primary key column for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
```

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.

# Solution

```
SELECT name, population, area
FROM World w
WHERE w.area >= 3000000 or w.population >= 25000000
```

Runtime: 385 ms, faster than 36.77% of MySQL online submissions for Big Countries.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Big Countries.
