#                       STARTING...

from time import sleep

print("DIRECTION: In Key, \n •Enter an 'integer' for Caeser Cipher \n •Enter any 'word' (without spaces) for simple Vigenère Cipher \n •Enter any 'Hashing algorithm' like 'sha1 or md5 or sha384 etc.' for Hashing. \n •Enter any 'sentence' for anvanced Vigenère Cipher.")
print()
print()

text = input("Text: ")
key = input("Key: ")

#                                     ___ASCII Cipher___

if key[1:].isnumeric() or key[0:].isnumeric():
    
    cipher = int(key)

    list=[]
    char=[]
    for num in text:
        list.append(ord(num)+cipher)
    for i in list:
        char.append(chr(i))

    enc_txt = ''.join(char)

#                                       ___Hashing #___

elif "sha" in key or "md5" in key:

    import hashlib

    key = str(key)

    if key == 'sha1':
        hash_object = hashlib.sha1(text.encode())
    elif key == 'sha256':
        hash_object = hashlib.sha256(text.encode())
    elif key == 'sha224':
        hash_object = hashlib.sha224(text.encode())
    elif key == 'sha384':
        hash_object = hashlib.sha384(text.encode())
    elif key == 'md5':
        hash_object = hashlib.md5(text.encode())
    elif key == 'sha512':
        hash_object = hashlib.sha512(text.encode())
    else:
        hash_object = hashlib.sha1(text.encode())

    enc_txt = hash_object.hexdigest()

#                                        ___Vigenère Cipher___                  Contains most ERRORs
else:
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    text_list = list(text)

    for char in text_list:       # removes the characters not in alpha like staces, fulstops eetc.
        if char not in alpha:
            text_list.remove(char)

    key = str(key)
    text = ''.join(text_list)

    key2 = key*(len(text)//len(key))
    remainder = len(text) % len(key)

    key_list = list(key2)            #These 5 lines along are mind blogging and complicated..

    for i in range(remainder):
        key_list.append(key_list[i])

    Key = ''.join(key_list)          #Till Here.

    plist = []                      #contains text indexes
    klist=[]                        #contains negative key indexes

    enc = []                        #contains their sum
    txt = []                        #contains chracters on indexes
    for i in text:
        plist.append(alpha.index(i))

    for k in Key:
        klist.append(alpha.index(k) - len(alpha))

    for num in range(len(plist)):
        enc.append(plist[num] + klist[num])                 # <- Error-some

    for index in enc:
        txt.append(alpha[index])

    enc_txt = ''.join(txt)

    #                           ...END

print("\n Here's the encrypted text:- \n \n \t",enc_txt)
print("________________________________")
print("\n Copy, paste, Enjoy!")

sleep(7)
