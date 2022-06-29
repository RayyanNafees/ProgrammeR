
# General math_______________________________

def factorial(num: int) -> int:
    '''Returns the factorial(!) of the supplied integer.'''
    '''Returns !num'''
    if num < 0:
        factorial = None

    elif num == 0:
        factorial = 1

    else:
        factorial = 1
        for i in range(1,num+1):
            factorial = factorial*i

    return factorial


def factorise(num: int) -> list:
    '''Returns a list of factors of the supplied integer.
    (except the integer itself and 1)'''

    factors = [i for i in range(2,num) if not num%i]
    return factors


def isprime(num: int)  -> bool:
    '''Checks whether the supplied integer is Prime or not.'''
    return not bool(factorise(num))


def prime_factorise(num: int) -> list:
    '''docstring'''
    prime_factors = []
    primez = [i for i in factorise(num) if isprime(i)]

    while num != 1:
        for n in primez:
            if num % n == 0:
                prime_factors.append(n)
                num /= n
    prime_factors.sort()

    return prime_factors


def fact_count(*nums) -> dict:
    '''Returns the prime factorisation of the supplied integers
       according to the Fundamental Theorem of Arithmetics'''
    '''fact_count(f**n,(x**y)*(a**b)) -> {f**n: {f:n}, (x**y)*(a**b): {x:y,a:b}}
       fact_count(32,36) -> {32: {2:5}, 36: {2:2,3:2}}'''
    pf = prime_factorise
    if nums:
        return {n: {f:pf(n).count(f) for f in set(pf(n))} for n in nums}


def primes(num: int) -> list:
    '''Returns a list of primes lying between 0 and the supplied no.'''

    primes = [i for i in range(2,num) if isprime(i)]

    return primes


def conjectures(num: int) -> list:
    '''Returns a list of multi Goldbach's Conjectures found for the supplied prime no.'''

    conjectures = []

    prime_list = primes(num)

    for p in prime_list:
        for k in prime_list:
            if p + k == num:
                conjectures.append(f'{p} + {k}')

    if not conjectures:
        for j in prime_list:
            for k in prime_list:
                for l in prime_list:
                    if j + k + l == num:
                        conjectures.append(f'{j} + {k} + {l}')


    from pprint import pprint

    return pprint(conjectures[:(len(conjectures)//2)] )


def HCF(x: int, y: int) -> set:
    '''Returns the HCF of the provided integers (x,y).'''
    setx = set(factorise(x))
    sety = set(factorise(y))

    Factor = setx.intersection(sety)

    return max(Factor) if bool(Factor) else 1

hcf = GCD = gcd = HCF


def lcm(x: int, y: int) -> int:
    '''Returns the least commom multiple(LCM) of the supplied integers'''
    for i in range(1,x*y+1):
        if i%x==0 and i%y==0:
            lcm = i
            break
    return lcm

LCM = lcm


# Statistics________________________________

def mean(*obs: tuple) -> float:
    '''Returns the mean (average) of the supplied list of observations.'''
    return sum(obs)/len(obs) if obs else 0


def median(*nums: list) -> int:
    '''Returns the mid-object of the supplied list.'''
    ltype = len(nums)%2
    mid_obj = len(nums)//2

    if ltype != 0:
        return nums[len(nums)//2]
    else:
        return (nums[mid_obj] + nums[mid_obj - 1])/2
