```
SELECT
ROUND(100.0 * SUM(CASE WHEN (call_category = 'n/a' OR call_category IS NULL) THEN 1 ELSE 0 END) / COUNT(*),1)
AS uncategorised_call_pct
FROM callers
```

Solution: Filter

```
SELECT
  ROUND (100.0 *
    COUNT (case_id) FILTER (
      WHERE call_category IS NULL OR call_category = 'n/a')
    / COUNT (case_id), 1) AS uncategorised_call_pct
FROM callers;
```
    