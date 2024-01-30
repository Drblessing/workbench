Solution: between and date casting

```sql
select user_id, max(post_date::date) - min(post_date::date) as days_between
from posts
where post_date between '2021-01-01' and '2021-12-31'
group by user_id
having count(post_id) > 1
```
