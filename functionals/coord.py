
def triarea(A: tuple, B: tuple, C: tuple) -> float:
    '''docstring'''
    return abs(0.5*( A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]) ))


def devide(*coords: tuple) -> tuple:
    '''Yields three coordinates of a triangle from the supplied coords.'''
    for i in range(2, len(coords)):
        yield (coords[0], coords[i-1], coords[i])


def area(*coords: tuple) -> float:
    '''docstring'''
    assert all(type(i) == tuple for i in coords), 'Supply tuples of coords: (x,y)'
    if len(coords) < 3: return 0
    return sum(triarea(a,b,c) for a,b,c in devide(*coords))
