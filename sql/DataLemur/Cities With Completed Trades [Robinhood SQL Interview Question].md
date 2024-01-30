Solution: Join

```sql
select city, count(order_id) as total_orders
from trades t
join users u on u.user_id = t.user_id
where t.status = 'Completed'
group by city
order by total_orders desc
limit 3 
```
