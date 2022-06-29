from time import sleep

enc_type = input('Is the text Ciphered(Y/N): ')

if enc_type == 'Y' or 'Yes' or 'y'or 'yes':
    phrase=list(str(input("\n Enter the encrypted text:- \n \n \t")))
    cipher=int(input('Key: '))
    list=[]
    char=[]
    for num in phrase:
        list.append(ord(num)-cipher)
    for i in list:
        char.append(chr(i))
    print("\n Here's the original txt:- \n \n \t",''.join(char))
else:
    print("Sorry! I could only decrypt ciphered TXT...")

sleep(5)
