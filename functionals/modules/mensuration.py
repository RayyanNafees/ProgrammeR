
def square(side: float=0, perimeter: float=0, area: float=0, diagonal: float=0) -> dict:
    '''Returns a dict of the remaining values from a supplied  value argument.'''
    values = {}

    if side:
        perimeter = 4*side
        area = side**2
        diagonal = (2*(side**2))**0.5

    elif perimeter:
        side = perimeter/4
        area = side**2
        diagonal = (2*(side**2))**0.5

    elif area:
        side = (area)**0.5
        perimeter = 4*side
        diagonal = (2*(side**2))**0.5

    elif diagonal:
        side = ((diagonal**2)/2)**0.5
        perimeter = 4*side
        area = side**2

    else:
        return('At least one argument value is required !')

    values = {}
    values['side'] = side
    values['perimeter'] = perimeter
    values['area'] = area
    values['diagonal'] = diagonal

    return values

def rectangle(l=0, b=0, area=0, peri=0, diag=0) -> float:
    '''Returns the remaining properties from the supplide values of a rectangle.
       where:   l= length, b= breadth, peri = perimeter'''


    if l and b:
        p = 2*(l+b)
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif l and a:
        p = 2*(l+b)
        b = a/l
        d = ((l**2)+(b**2))**0.5

    elif b and a:
        p = 2*(l+b)
        l = a/b
        d = ((l**2)+(b**2))**0.5

    elif l and p:
        b = p/2 - l
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif p and b:
        l = p/2 - b
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif l and d:
        p = 2*(l+b)
        a = l*b
        b = ((d**2)-(l**2))**0.5

    elif d and b:
        p = 2*(l+b)
        a = l*b
        l = ((d**2)-(b**2))**0.5

    elif a and p:
        for ln in range(max(a,p)+1):
            for bd in range(max(a,p)+1):
                if ln+bd == p/2 and ln*bd == a:
                    l,b = ln,bd
                    break
        d = ((l**2)+(b**2))**0.5

    elif d and p:
        for ln in range(max(d,p)+1):
            for bd in range(max(d,p)+1):
                if ln+bd == p/2 and ((ln**2)+(bd**2))**0.5 == d:
                    l,b = ln,bd
                    break
        a = l*b

    elif d and a:
        for ln in range(max(d,a)+1):
            for bd in range(max(d,a)+1):
                if ln*bd == a and ((ln**2)+(bd**2))**0.5 == d:
                    l,b = ln,bd
                    break
        p = 2*(l+b)

    prop = {}
    prop['length'] = l
    prop['breadth'] = b
    prop['area'] = a
    prop['perimeter'] = p
    prop['diagonal'] = d

    return prop
