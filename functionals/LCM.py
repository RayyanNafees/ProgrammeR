
from prime_factoriser import prime_factorise as pf
from HCF import hcf


def prod(iterable) -> int:
    num = 1
    for n in iterable: prod *= n
    return prod


def lcm(x: int, y: int) -> int:
    '''Returns the least commom multiple(LCM) of the supplied integers'''
    for i in range(1,x*y+1):
        if i%x==0 and i%y==0:
            lcm = i
            break
    return lcm


Lcm = lambda n,m: n*m//hcf(n,m)


# innova:



fact_count = lambda *nums: {n: {f: pf(n).count(f) for f in set(pf(n))} for n in nums}

def factorisation(*nums: int) -> dict: pass
    

LCM = lambda *nums: prod(k*max(v) for k,v in factorisation(nums).items())

Hcf = lambda *nums: prod(k*min(v) for k,v in factorisation(nums).items()\
                if len(v) == len(nums))
