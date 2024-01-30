```
WITH call_records AS (SELECT policy_holder_id
FROM callers
GROUP BY policy_holder_id
HAVING COUNT(case_id) >= 3)

SELECT COUNT(policy_holder_id) as member_count
FROM call_records
```
