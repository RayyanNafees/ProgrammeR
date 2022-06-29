
from time import sleep
from random import randint

condition = input("Looking for probability of _")

int = randint(0,100)

#               ___COMMENT,S start___

if int >= 90:
    comment = '"Totally Certain!!"'
elif int < 90 and int >= 70:
    comment = '"very Likely!"'
elif int < 70 and int >= 60:
    comment = '"Likely"'
elif int < 60 and int > 40:
    comment = '"Even Chance!"'
elif int <= 40 and int > 20:
    comment = '"Unlikely.."'
elif int <=20 and int >= 10:
    comment = '"Very Unikely..."'
elif int < 10:
    comment = '"IMpossible ?"'
else:
    comment = ""

#           ___COMMENT,S end___

print("\n The probability for '",condition,"'is",str(int)+'%.')
print()
print("\t"*3,comment)

sleep(6)
