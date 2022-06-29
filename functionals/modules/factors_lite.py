
def prod(nums: list) -> int:
    '''Returns the product of integers in the supplied iterablr.'''
    prod =1
    for i in nums: prod*=i
    return prod

factorial = lambda num: prod(range(1,num+1)) if num >= 2 else 1

factorise = lambda num: [i for i in range(2,num) if not num%i]

isprime = lambda num: not bool(factorise(num))

primes = lambda num: [n for n in range(2,num) if isprime(n)]

primes_in = lambda num: {n for n in factorise(num) if isprime(n)} if not isprime(num) else {num}


def nearest_prime(prime: int) -> int:
    '''Returns the prime on the no. line nearest (and greatest) to the supplied prime.'''
    
    while True:
        prime += 1
        if isprime(prime): break

    return prime


def prime_factorise(num: int) -> tuple:
    '''Returns the prime factors of the supplied integer.'''
    factors = []

    for i in primes_in(num):
        while not num%i:
            factors.append(i)
            num //= i

    return tuple(sorted(factors))


pf = prime_factorise

fact_count = lambda num: {f: pf(num).count(f) for f in pf(num)}

fact_counts = lambda *nums: {n: fact_count(n) for n in nums}

factorisation = lambda *nums: {f : [i.get(f,0) for i in fact_counts(*nums).values()] for f in primes_in(prod(nums))}

lcm = lambda *nums: prod(k ** max(v) for k,v in factorisation(*nums).items())

hcf = lambda *nums: prod(k ** min(v)  for k,v in factorisation(*nums).items() if len(v) == len(nums))
