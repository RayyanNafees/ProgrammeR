#DRAWBACK: can't take negative list index values,
#so gets crashed if gets 2 alphabets whose sum of indexes is more than '26'.

alpha = list('abcdefghijklmnopqrstuvwxyz')

phrase = list('bolblearn')
key = list('webwebweb')

plist = []
klist = []

txt = []

for i in phrase:
    plist.append(alpha.index(i))

for j in key:
    klist.append(alpha.index(j))

for t in range(len(phrase)):
    txt.append(alpha[plist[t] + klist[t]])

print(''.join(txt))
    
