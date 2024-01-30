Solution: Round to million and use CONCAT to convert number into string.

```
SELECT manufacturer, CONCAT('$',ROUND(sum(total_sales)/1000000), ' million') as sales_mil
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC
```
