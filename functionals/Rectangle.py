
def rectangle(length: float=0, breadth: float=0, area: float=0, perimeter: float=0, diagonal: float=0) -> float:
    """Returns the remaining properties from the supplide values of a rectangle."""
    l= length
    b= breadth
    a= area
    d= diagonal
    p= perimeter

    if bool(l)==True and bool(b)==True:
        p = 2*(l+b)
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif bool(l)==True and bool(a)==True:
        p = 2*(l+b)
        b = a/l
        d = ((l**2)+(b**2))**0.5

    elif bool(b)==True and bool(a)==True:
        p = 2*(l+b)
        l = a/b
        d = ((l**2)+(b**2))**0.5

    elif bool(l)==True and bool(p)==True:
        b = p/2 - l
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif bool(p)==True and bool(b)==True:
        l = p/2 - b
        a = l*b
        d = ((l**2)+(b**2))**0.5

    elif bool(l)==True and bool(d)==True:
        p = 2*(l+b)
        a = l*b
        b = ((d**2)-(l**2))**0.5

    elif bool(d)==True and bool(b)==True:
        p = 2*(l+b)
        a = l*b
        l = ((d**2)-(b**2))**0.5

    elif bool(a)==True and bool(p)==True:
        for ln in range(max(a,p)+1):
            for bd in range(max(a,p)+1):
                if ln+bd == p/2 and ln*bd == a:
                    l,b = ln,bd
                    break
        d = ((l**2)+(b**2))**0.5

    elif bool(d)==True and bool(p)==True:
        for ln in range(max(d,p)+1):
            for bd in range(max(d,p)+1):
                if ln+bd == p/2 and ((ln**2)+(bd**2))**0.5 == d:
                    l,b = ln,bd
                    break
        a = l*b

    elif bool(d)==True and bool(a)==True:
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

    
