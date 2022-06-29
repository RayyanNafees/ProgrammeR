def triangle(a: float, b: float=0, c: float=0, perimeter: float, area: float=0, altitude: float=0) -> dict:
    """Returns the area of the triangle from the supplied mesurments."""
    """Recommended: 'Use keyword assignments for assigning entries'"""
    """The 1st 3 arguments (a,b,c) reffers to the three sides of a triangle."""

    if bool(a) and bool(b) and bool(c) == True:
        s = (a+b+c+)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        altitude = (2*area)/b
        perimeter = a+b+c

    elif bool(a) and bool(b) and bool(area) == True or bool(c) and bool(b) and bool(area) == True or bool(a) and bool(c) and bool(area) == True:
        
    
