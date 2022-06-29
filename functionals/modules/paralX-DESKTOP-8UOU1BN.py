
from math import pi, sin, tan

Rad = lambda deg: deg/180*pi
Deg = lambda rad: rad/pi*180

def dist(basis, angL, angR, unit = 'deg', dp = None):
    '''Returns the altitude of the triangle from the supplied:
    angles (at the basis), basis-lenght, dp (decimal place)
    accepted angular units: 'deg', 'rad', 'grad'
    [!ALERT!: angles measured should be of the same point on the obj.]'''
    if unit == 'deg':
        x,y,z = Rad(angL), Rad(angR), Rad(180-angL-angR)
    elif unit == 'rad':
        x,y,z = angL, angR, Rad(180 -Deg(angL)-Deg(angR))

    if not z: return basis

    s_z = basis                      # side opposite to z
    s_y = abs(sin(y)/sin(z))*basis   # side opposite to y
    s_x = abs(sin(x)/sin(z))*basis   # side opposite to x
    sp  = (s_x + s_y + s_z)*0.5      # semi-perimeter
    area= (sp*(sp - s_x)*(sp - s_y)*(sp - s_z))**0.5    # area by Heron's formula
    alt = (2*area)/basis if basis else 0                # Using relation [area = (1/2)*basis*alt]
    print(alt)
    return float(f'%.{dp}f'%alt) if dp != None else alt


cot = lambda ang: tan(ang)**(-1)
dist2 = lambda basis, angL, angR: basis/(cot(Rad(angL)) + cot(Rad(angL)))   # Angles must be in degrees...
# dist2(x)*2 == dist(x)


def height(basis, Dist, angL, angR, unit = 'deg', dp = None):
    '''Returns the altitude of the triangle from the supplied:
    angles (at the basis), basis-lenght, dp (decimal place)
    accepted angular units: 'deg', 'rad', 'grad'
    [!ALERT!: angles measured should be of the obj's extreme top&left corners.]'''
    if unit == 'rad': angL, angR = Deg(angL), Deg(angR)
    size = angL + angR
    if size == 180: return basis
    if size > 180:
        x,y = basis, dist(basis, 180-angL, 180-angR)
        return (y+Dist)/y*x
    else:
        x,y = basis, dist(basis, angL, angR)
        return (y-Dist)/y*x


# linear version of heioght; using realtion:   ['+' if (angL+angR) > 180 else '-']
# height = (dist +/- (y:= dist(basis, 180 +/- angL, 180 +/- angR)))/y*basis
# ['+' if (angL+angR) > 180 else '-']; angles are to be expressed in Degrees...

#lenght = lambda basis, Dist, angL, angR: ((y:= dist(basis, *(180-angL,180-angR if s>180 else angL,angR)))+Dist if (s:= angl+angR)>180 else y-Dist)/y*basis
                                         

def less_numeric(num: float, lim=3):
    '''Returns (y,x) ; for y*(x**0.5) == num'''
    from itertools import count
    for root in count(2):
        for i in count(1):
            x = i**(1/root)
            y = num/x
            if int(y) == float(y): return (int(y),i,root)
            if i > lim: break

simpler = lambda num: f'{less_numeric(num)[0]}_/{less_numeric(num)[1]}'
