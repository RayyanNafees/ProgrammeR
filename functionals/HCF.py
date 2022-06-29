
factorise = lambda num: [i for i in range(2,num) if not num%i]

def GCD(x:int, y:int) -> set:
    """Returns the GCD of the provided integers (x,y)."""
    setx = set([1]+factorise(x)+[x])
    sety = set([1]+factorise(y)+[y])

    Factor = setx.intersection(sety)
    return max(Factor)


def hcf(num1: int, num2: int) -> int:
    '''Returns the hcf of the supplied integers.
       Using "Euclid's Devision lemma": (a = b*q + r ; 0 <= r < b)'''
    a,b = (num1,num2) if num1>num2 else (num2,num1)
    q = a//b
    r = a - b*q

    if r == 0:
        return b
    else:
        return hcf(b,r)
