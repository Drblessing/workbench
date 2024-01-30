```sql
select candidate_id from candidates
where skill in ('Python','Tableau','PostgreSQL')
group by candidate_id
having count(skill) = 3
order by candidate_id;
```

Complex Solution

```sql
SELECT candidate_id
FROM (
  SELECT candidate_id, ARRAY_AGG(skill::text) AS skills
  FROM candidates
  GROUP BY candidate_id
) AS subquery
WHERE ARRAY['Python', 'Tableau', 'PostgreSQL']::text[] <@ skills
ORDER BY candidate_id;
```
