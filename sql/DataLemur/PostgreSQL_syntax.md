# PostgreSQL 14

## Basics

Strings are denoted with single-quotes. 'string here'.

For string methods, like `where`, you can use a tuple:

```
WHERE skill IN ('Python', 'Java')
```

]

Round numbers in digits by dividing by the whole digit then round to 0.
For example, to convert numbers to millions:

```
ROUND(sum(total_sales)/1000000)
```

Turn numbers into strings with `CONCAT`:

```
CONCAT('$',ROUND(sum(total_sales)/1000000), ' million')
```

### CTE

Can cache results of a query for later use. Useful for complex queries that are used multiple times.

```

WITH jobs_grouped AS (
-- Insert above query here
SELECT
company_id,
title,
description,
COUNT(job_id) AS job_count
FROM job_listings
GROUP BY
company_id,
title,
description;

)

```

SELECT COUNT(DISTINCT company_id) AS co_w_duplicate_jobs
FROM jobs_grouped
WHERE job_count > 1;

```

```

## Functions

```

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

```

## Keywords

### Exists / Not Exists

Corerlated subquery, condition in the nested subquery

```

SELECT l.\*
FROM t_left l
WHERE NOT EXISTS
(
SELECT NULL
FROM t_right r
WHERE r.value = l.value
)

```

### SUM

Aggregate function that will sum numerical value

### Count

Will count rows, even blank ones

### CASE

Syntax:

```

CASE WHEN [Condition] THEN [true value] ELSE [false value] END

```

Example:

```

CASE WHEN device_type in ('tablet','phone') THEN 1 ELSE 0 END

```

## Dates

### Get year from date

```

WHERE date_part('year',post_date) = 2021

```

### Number of days between timestamps

```
MAX(post_date::DATE) - MIN(post_date::DATE) as days_between
```

### Get Month and Year from date

```
WHERE EXTRACT(MONTH FROM sent_date) = '8'
  AND EXTRACT(YEAR FROM sent_date) = '2022'
```
