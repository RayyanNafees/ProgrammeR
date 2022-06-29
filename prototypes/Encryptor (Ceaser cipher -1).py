phrase = input()
list = []
char = []
for num in phrase:
    list.append(ord(num)-1)
for i in list:
    char.append(chr(i))
print(''.join(char))
