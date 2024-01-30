```
SELECT manufacturer, COUNT(drug), SUM(cogs - total_sales) as total_loss
FROM pharmacy_sales
WHERE total_sales - cogs < 0
GROUP BY manufacturer
ORDER BY total_loss DESC
```
