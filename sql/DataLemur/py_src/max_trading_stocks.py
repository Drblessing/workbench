def max_subarray_sum(prices: list[int]) -> int:
    """Calculate the maximum profit from a list of stock prices."""

    # Handle edge cases
    if len(prices) < 2:
        return 0

    # Initialize the maximum profit to 0
    max_profit = 0
    # Keep track of the minimum prices seen up to the current index
    min_prices = prices[0]

    # Iterate over the prices
    for price in prices:
        # Update the minimum price seen
        min_prices = min(min_prices, price)
        # Update the maximum profit seen
        max_profit = max(max_profit, price - min_prices)

    # Return the maximum profit
    return max_profit
