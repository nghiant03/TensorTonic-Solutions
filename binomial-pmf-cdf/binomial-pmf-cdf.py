import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    p_k = math.comb(n, k) * pow(p, k) * pow(1-p, n-k)
    p_lk = 0
    for i in range(k+1):
        p_lk += math.comb(n, i) * pow(p, i) * pow(1-p, n-i)
        
    return {"pmf": float(p_k), "cdf": float(p_lk)}