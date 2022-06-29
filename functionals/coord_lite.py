
triarea = lambda A,B,C : abs(0.5*( A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]) ))

devide = lambda *coords: ((coords[0], coords[i-1], coords[i]) for i in range(2, len(coords)))

area   = lambda *coords: 0 if len(coords) < 3 else sum(triarea(a,b,c) for a,b,c in devide(*coords))
