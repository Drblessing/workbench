import statistics
import math


def corr(x: list[int | float], y: list[int | float]) -> float:
    """Returns the correlation coefficient of two lists of numbers."""
    if len(x) != len(y):
        raise ValueError("Vectors must be the same length.")
    n = len(x)
    if n == 0:
        raise ValueError("Vectors must not be empty.")
    x_mean = statistics.mean(x)
    y_mean = statistics.mean(y)
    x_std = statistics.stdev(x)
    y_std = statistics.stdev(y)
    if x_std == 0 or y_std == 0:
        return 0
    return sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n)) / (
        (n) * x_std * y_std
    )
