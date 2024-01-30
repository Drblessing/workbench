Solution: RANK

```
WITH product_rank AS (SELECT category,
product,
SUM(spend),
RANK() OVER (PARTITION BY category ORDER BY SUM(spend) DESC) as rank1
FROM product_spend
WHERE transaction_date >= '2022-01-01'
  AND transaction_date <= '2022-12-31'
GROUP BY category,product)

SELECT category,product,sum as total_spend
FROM product_rank
WHERE rank1 < 3
```
