from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    counter = Counter(x)
    mode = max(counter, key=counter.get)
    mean = sum(x) / len(x)
    x = sorted(x)
    median = x[len(x) // 2 ] if len(x) % 2 == 1 else (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
    return {"mean": float(mean), "median": float(median), "mode": float(mode)}