Solution: Extract within group by clause

```
SELECT EXTRACT(MONTH FROM submit_date) as mth,product_id as product,ROUND(AVG(stars),2) as avg_stars
FROM reviews
GROUP BY EXTRACT(MONTH FROM submit_date), product_id
ORDER BY EXTRACT(MONTH FROM submit_date),product_id ASC
```
