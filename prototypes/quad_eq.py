
print('In the Quadratic Equation: "ax^2 + bx + c = 0", the values of :-') 

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

zero = []
for num in range(-1*(a*c),(a*c)):
    for num2 in range(-1*(a*c),(a*c)):
        if num + num2 == b and num*num2 == c:
            zero += [num,num2]

if zero[0] == zero[-1]:
    print(zero[0])
else:
    print(zero)
