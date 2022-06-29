
for i in (chr(c) for c in range(65, 65+5)):
    exec(f'{i.lower()} = lambda i: print(i)')
