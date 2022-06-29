
factorise = lambda num: [i for i in range(2,num) if not num % i]

isprime = lambda num: not bool(factorise(num))


def prime_factorise(num: int) -> list:
    '''docstring'''
    if isprime(num): return (num)

    factors = []
    for prime in (n for n in factorise(num) if isprime(n)):
        while not num % prime:
            factors.append(prime)

    return sorted(tuple(factors))
