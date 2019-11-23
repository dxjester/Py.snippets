"""
FILENAME: functions_algorithms.py
PROJECT: Py.snippets
DATE CREATED: 17-NOV-19
DATE UPDATED: 9-NOV-19
VERSION: 1.0
"""

# CATEGORY: numpy, prime, numbers, 
# DESCRIPTION: sieve algorithm
from math import sqrt

def sieve(n):
    """
    Returns the prime number 'sieve' shown above.
    
    That is, this function returns an array `X[0:n+1]`
    such that `X[i]` is true if and only if `i` is prime.
    """
    is_prime = np.empty(n+1, dtype=bool) # the "sieve"

    # Initial values
    is_prime[0:2] = False # {0, 1} are _not_ considered prime
    is_prime[2:] = True # All other values might be prime

    # Implement the sieving loop
    for k in range(2, int(sqrt(n))+1):
        is_prime[2*k::k] = False
    
    return is_prime

# Prints your primes
print("==> Primes through 20:\n", np.nonzero(sieve(20))[0])