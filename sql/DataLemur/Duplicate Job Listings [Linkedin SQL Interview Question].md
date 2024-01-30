Solution 1: Subquery with group by

```sql
select count(distinct company_id) as duplicate_companies
from (select company_id
from job_listings
group by title,description, company_id
having count(company_id) > 1) j1
```

Solution 2: CTE

```sql
with job_count_cte as (
  select company_id,title,description,count(job_id) as job_count
  from job_listings
  group by company_id, title, description
  having count(job_id) > 1)

select count(distinct company_id) as duplicate_companies
from job_count_cte
```
