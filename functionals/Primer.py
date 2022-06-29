
def prime(num:int)  ->str:
    '''Tells whether the supplied integer is Prime or Composite. If Composite, How?'''

    print()
    ans = []

    for i in range(2,num):
        if num % i == 0:
            ans.append(False)
            factor = i
        else:
            ans.append(True)

    if False not in ans:
        print('Yes,',num,'is Prime!')
    else:
        print('No,',num,'is Composite! \n  ',num//factor,'times',factor,'is',num)

# Linear________
factorise = lambda num: [i for i in range(2,num) if num%i == 0]
isprime = lambda num: not bool(factorise(num))
