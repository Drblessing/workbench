```sql
SELECT page_id
FROM pages
WHERE NOT EXISTS (SELECT NULL FROM page_likes WHERE page_likes.page_id = pages.page_id)
ORDER BY page_id;
```

Solution 2: Left Outer Join

```sql
SELECT pages.page_id
FROM pages
LEFT OUTER JOIN page_likes AS likes
  ON pages.page_id = likes.page_id
WHERE likes.page_id IS NULL;
```

Solution 3: Using EXCEPT

```sql
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes
ORDER BY page_id;
```

Solution 4: Using NOT IN

```sql
select page_id
from pages
where page_id not in (
select page_id
from page_likes)
order by page_id
```
