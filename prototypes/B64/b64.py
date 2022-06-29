
def b64to10(b64, base=64):
    vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    #return sum([...b64].map((b,n)=> vals.indexOf(b)*pow(base, b64.length-1-n)))
    [print(i) for i in b64 if i not in vals]
    return sum(vals.index(b)*(base**(len(b64)-1-n)) for n,b in enumerate(b64))


def nearest_even(n) :
    'Returns the higest power of 2 less than n'
    i=0
    while n - pow(2, i+1)>=0:
        i+=1
    return i


def nearest_pow(num: int, base: int=2):
    'Returns the higest power of int less than num'
    i=0
    while num - pow(base, i+1)>=0:
        i+=1
    return i


def nearest_pow_num(n: int, base: int):
    'Returns [X = highest power of base less than n, highest multiple of 3*X less than n]'
    nums = list(reversed(range(base)))
    i=0
    p = nearest_pow(n,base)
    while True:
        if (pow(base, p) * nums[i]) <=n:
            return [p, nums[i]]
        i+=1


def nearest_char_pow_num(n: int, chars: list):
    chars =list( reversed(chars))
    nums =  list(reversed(range(len(chars))))
    i = 0
    base = len(chars)
    p = nearest_pow(n,base)
    while True:
        if pow(base,p) * nums[i] <= n:
            return [chars[i], p, nums[i]]
        i += 1


def b10to2 (dec: int):
    pows = {}
    while dec:
        _pow = nearest_even(dec)
        pows[_pow]=1
        dec -= pow(2,_pow)
    intarr = [0 for i in range(max(pows)+1)] # make an array of 0s (length = highest power of 2 divisible by dec)
    for p in pows.items():
        intarr[p] = 1
    return ''.join(reversed(intarr))


def b10to3 (dec) :
    pows = {}
    while dec:
        _pow, mul = nearest_pow_num(dec, 3)
        pows[_pow] = mul
        dec -= mul*pow(3,_pow)

    intarr = [0 for i in range(max(pows)+1)] # make an array of 0s (length = highest power of 2 divisible by dec)
    for p,m in pows.items():
        intarr[p] = m
    return ''.join(reversed(intarr))


def b10toN (dec: int, N=2):
    assert 10 >= N >=2, "N must be 10 >= N >= 2"
    pows = {}
    while dec:
        p,m = nearest_pow_num(dec, N)
        pows[p] = m
        dec -= m*pow(N,p)

    intarr = [0 for i in range(max(pows)+1)] # make an array of 0s (length = highest power of 2 divisible by dec)
    for p,m in pows.items():
        intarr[p] = m
    return ''.join(reversed(intarr))


def b10toAny(dec, chars) :
    N = len(chars)
    assert N >=2, "N must be N >= 2"
    pows={}
    while dec:
        [_pow, mul] = nearest_pow_num(dec, N)
        pows[_pow] = mul
        dec -= mul*pow(N,_pow)

    intarr = [0 for i in range(max(pows)+1)] # make an array of 0s (length = highest power of 2 divisible by dec)
    for p,m in pows.items():
        intarr[p] = chars[m]
    return ''.join(reversed(intarr))


b10to64 = lambda dec: b10toAny(dec, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')