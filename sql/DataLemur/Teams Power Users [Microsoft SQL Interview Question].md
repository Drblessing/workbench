Solution: Extract date, group

```sql
SELECT sender_id,COUNT(message_id) as message_count
FROM messages m1
WHERE EXTRACT(MONTH FROM sent_date) = 08 AND
EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY sender_id
ORDER BY COUNT(*) DESC
LIMIT 2
```

Solution: Between

```sql
select sender_id, count(*) as count_messages
from messages
where sent_date between '2022-08-01' and '2022-08-31'
group by sender_id
order by count(*) desc
limit 2
```
