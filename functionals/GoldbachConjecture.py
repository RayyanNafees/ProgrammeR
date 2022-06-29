
def factorise(num:int) -> list:
    """Returns a list of factors of the supplied integer.
    (except the integer itself and 1)"""

    factors = []

    for i in range(2,num):
        if num % i == 0:
            factors.append(i)

    return factors


def primes(num: int) -> list:
    """Returns a list of primes lying between 0 and the supplied no."""

    primes = []

    for i in range(2,num):
        if bool(factorise(i)) == False:
            primes.append(i)

    return primes

def biconject(num: int) -> list:
    """Returns a list of multi Goldbach's Conjectures found for the supplied prime no."""

    conjectures = []

    prime_list = primes(num)

    for p in prime_list:
        for k in prime_list:
            if p + k == num:
                conjectures.append((p,k))

    if not conjectures:
        for j in prime_list:
            for k in prime_list:
                for l in prime_list:
                    if j + k + l == num:
                        conjectures.append((j,k,l))


    from pprint import pprint

    return pprint(conjectures[:(len(conjectures)//2)] )
