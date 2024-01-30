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

Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

# Solution

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee e
      ORDER BY salary DESC
      LIMIT M,1
  );
END
```

We have to declare M because arithmetic cannot be done in the LIMIT statement, also, because this is a return statement we don't have to handle the null value.
