

def sum(iterable: object, /) -> object:
    '''
    Returns the sum of the objects (rather than only integers in BIF 'sum')
    in the supplied iterable. (if the have __add__ attribute or supports concatenation)
    '''
    obj = list(iterable)[0]
    assert '__add__' in dir(obj), \
           'The supplied iterable has inconcatenable or inaddable objects!'

    prime = type(obj)()
    for i in list(iterable):
        prime += i

    return prime



def prod(nums: list) -> object:
    '''Returns the product of integers in the supplied iterable.'''
    prod =1
    for i in nums: prod*=i
    return prod


def factorial(num: int) -> int:
    '''Returns num! (factorial of the supplied num)'''
    return prod(range(1,num+1)) if num > 1 else 1


def factorise(num: int) -> list:
    '''Returns all the composite/prime factors in the supplied number.'''
    return [i for i in range(2,num) if not num%i]


def isprime(num: int) -> bool:
    '''Tells whether the supplied number is prime or not.'''
    return not bool(factorise(num))


def primes(num: int) -> list:
    '''Returns a list of prime numbers from 2 to the supplied number.'''
    return [n for n in range(2,num) if isprime(n)]


def primes_in(num: int) -> set:
    '''Returns a set of prime numbers in the supplied number.'''
    return {n for n in factorise(num) if isprime(n)} if not isprime(num) else {num}



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


def fact_count(num: int) -> dict:
    '''Returns a dict of factors and their quantity in the composite numeral.'''
    return {f: pf(num).count(f) for f in pf(num)}


def fact_counts(*nums: int) -> dict:
    '''Returns a dict of factors and their quantity in the list of composite numerals.'''
    return {n: {f: pf(n).count(f) for f in pf(n)} for n in nums}


def factorisation(*nums: int) -> dict:
    '''Returns a dict of'''
    return {f : [i.get(f,0) for i in fact_counts(*nums).values()] for f in primes_in(prod(nums))}


def lcm(*nums: int) -> int:
    '''Returns the LCM of the supplied integers.'''
    return prod(k ** max(v) for k,v in factorisation(*nums).items())


def hcf(*nums: int) -> int:
    '''Returns the HCF (or GCD) of the supplied integers.'''
    return prod(k ** min(v)  for k,v in factorisation(*nums).items())
