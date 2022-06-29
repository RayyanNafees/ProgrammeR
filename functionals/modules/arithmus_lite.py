
# General math_______________________________

def factorial(num: int) -> int:
    '''Returns the factorial(!) of the supplied integer.'''
    '''Returns !num'''
    if num < 0:    return None
    elif num == 0: return 1
    else:
        factorial = 1
        for i in range(1,num+1): factorial *= i

        return factorial

factorise = lambda num: [i for i in range(2,num) if not num%i]

isprime = lambda num: not bool(factorise(num))

primes = lambda num: list(filter(isprime, range(2,num)))


def prime_factorise(num: int) -> list:
    '''docstring'''
    prime_factors = []
    primez = list(filter(isprime,factorise(num)))

    if isprime(num) == False:

        while num != 1:
            for n in primez:
                if num % n == 0:
                    prime_factors.append(n)
                    num /= n
        prime_factors.sort()

        return prime_factors
    else:
        return []

pf = prime_factorise


fact_count = lambda *nums: {n: {f:pf(n).count(f) for f in set(pf(n))} for n in nums} if nums else {}


def conjectures(num: int) -> list:
    '''Returns a list of multi Goldbach's Conjectures found for the supplied prime no.'''

    conjectures = []

    prime_list = primes(num)

    for p in prime_list:
        for k in prime_list:
            if p + k == num:
                conjectures.append(str(p)+' + '+str(k))

    if not bool(conjectures):
        for j in prime_list:
            for k in prime_list:
                for l in prime_list:
                    if j + k + l == num:
                        conjectures.append(str(j)+' + '+str(k)+' + '+str(l))


    from pprint import pprint

    return pprint(conjectures[:(len(conjectures)//2)] )


def HCF(num1: int, num2: int) -> set:
    '''Returns the HCF of the provided integers (x,y).'''
    setx = set(factorise(x))
    sety = set(factorise(y))

    return max(Factor) if (Factor := setx.intersection(sety)) else 1
    

GCD = gcd = hcf = HCF       # GCD = Greatest Common Dividend


def lcm(x: int, y: int) -> int:
    '''Returns the least commom multiple(LCM) of the supplied integers'''
    for i in range(1,x*y+1):
        if not all(i%x, i%y):
            lcm = i
    return lcm

LCM = lcm


# Statistics________________________________

mean = lambda *obs: sum(obs)/len(obs) if obs else 0

def median(*nums: tuple) -> int:
    '''Returns the mid-object of the supplied list.'''
    ltype = len(nums)%2
    mid_obj = len(nums)//2

    if ltype != 0:
        return nums[len(nums)//2]
    else:
        return (nums[mid_obj] + nums[mid_obj - 1])/2
