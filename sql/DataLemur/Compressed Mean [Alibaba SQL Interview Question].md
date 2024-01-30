Solution: Turn int into float

```
SELECT ROUND(1.0 * SUM(item_count*order_occurrences) / SUM(order_occurrences),1)
FROM items_per_order
```
