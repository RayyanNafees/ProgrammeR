
def hcf(a,b):
    a,b = (a,b) if a>b else (b,a)
    q = a//b
    r = a - b*q
    return b if r == 0 else hcf(b,r)


def rationalise(num: float) -> str:
    '''docstring'''
    p = int(str(num).replace('.',''))
    q = 10**len(str(num).split('.')[1])
    P = p// hcf(p,q)
    q //= hcf(p,q)
    return f'{P}/{q}'
