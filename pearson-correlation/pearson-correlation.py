import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X)
    X_c = X - np.mean(X, axis=0)
    variance = X_c.T @ X_c
    deviation = np.sqrt(np.sum(np.square(X_c), axis=0, keepdims=True))
    return variance / (deviation.T @ deviation)