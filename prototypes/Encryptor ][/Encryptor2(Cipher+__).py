from time import sleep

phrase = str(input("Enter your text:- \n \n \t"))
cipher = int(input('Key: '))

list=[]
char=[]
for num in phrase:
    list.append(ord(num)+cipher)
for i in list:
    char.append(chr(i))
print("\n Here's your encrypted txt. Copy, Paste and Send!:- \n \n \t",''.join(char))
sleep(5)
