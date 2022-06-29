with open('out.py','w') as out:
    print(list(map(lambda x: x+2,[1,2,3,4,5])),file = out)