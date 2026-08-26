import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    sum_deviation = np.sum(np.square(x-mean))
    variance = sum_deviation / (len(x) - 1)
    return {"variance": variance.item(), "standard_deviation": np.sqrt(variance).item()}