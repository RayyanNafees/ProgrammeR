
def square(side: float=0,
           perimeter: float=0,
           area: float=0,
           diagonal: float=0) -> dict:
    """Returns a dict of the remaining values from a supplied  value argument."""
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
        return {}

    values['side'] = side
    values['perimeter'] = perimeter
    values['area'] = area
    values['diagonal'] = diagonal

    for k,v in values.copy().items():
        if type(v) == float:
            values[k] = float('%.2f'%v)

    return values
