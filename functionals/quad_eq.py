
def quad_eq(a: int, b: int, c: int) -> list:
    '''In the Quadratic Equation: 'ax^2 + bx + c = 0',
    supply the values of a, b & c.''' 

    a = int(a)
    b = int(b)
    c = int(c)

    zero = []
    if b < 0:
        for num in range(-1*(a*c),(a*c)):
            for num2 in range(-1*(a*c),(a*c)):
                if num + num2 == b and num*num2 == c:
                    zero.extend([num,num2])

    if zero[0] == zero[-1]:
        return zero[0]
    else:
        return zero

# LIMITATION: can't calculate if either of 'a' or 'c' is negative. 
