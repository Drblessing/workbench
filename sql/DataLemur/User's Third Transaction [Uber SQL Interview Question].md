Solution: ROW_NUMBER, RANK, DENSE_RANK, CTE

```
WITH transaction_ranks AS (SELECT *,
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS transaction_rank
FROM transactions)

SELECT user_id,spend,transaction_date
FROM transaction_ranks
WHERE transaction_rank = 3
```
