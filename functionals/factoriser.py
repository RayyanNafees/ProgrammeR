
# Sparse
def factorise(num:int) -> list:
    """Returns a list of factors of the supplied integer.
    (except the integer itself and 1)"""

    factors = list(filter(lambda i: not num%i, range(2,num)))

    return factors

# Linear(func.al)
Factorise = lambda num: list(filter(lambda i: not num%i, range(2,num)))

# Comprehensional
factorise = lambda num: [i for i in range(2,num) if not num%i]
