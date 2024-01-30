```
SELECT
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
  SUM(CASE WHEN device_type IN ('tablet','phone') THEN 1 ELSE 0 END) AS mobile_views
FROM viewership;
```

Solution #2: Count filter

```sql
select
  count(*) filter (where device_type = 'laptop') as laptop_views,
  count(*) filter (where device_type in ('tablet','phone')) as mobile_views
from viewership;
```
