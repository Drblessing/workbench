Table: Employee

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.
```

Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

# Solution

1.

```
SELECT max(Salary) SecondHighestSalary
FROM Employee
WHERE Salary < (Select max(Salary) from Employee)
```

2.

```
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
```

3.

```
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```
