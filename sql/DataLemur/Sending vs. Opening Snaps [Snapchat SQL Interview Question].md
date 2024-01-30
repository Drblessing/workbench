SOLUTION: SUM FILTER

```
WITH age_totals AS (SELECT a2.age_bucket,
SUM(a.time_spent) FILTER (WHERE a.activity_type = 'send') AS sending,
SUM(a.time_spent) FILTER (WHERE a.activity_type = 'open') AS opening
FROM activities a
INNER JOIN age_breakdown a2 on a.user_id = a2.user_id
GROUP BY age_bucket)

SELECT age_bucket,
ROUND(100.0*sending / (sending+opening),2) AS send_perc,
ROUND(100.0*opening / (sending+opening),2) AS open_perc
FROM age_totals
```
