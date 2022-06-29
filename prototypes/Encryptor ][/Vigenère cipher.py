text = input("Text: ")
key = input("Key: ")


alpha = 'abcdefghijklmnopqrstuvwxyz'
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text_list = list(text)

key = str(key)
text = ''.join(text_list)

key2 = key*(len(text)//len(key))
remainder = len(text) % len(key)

key_list = list(key2)            #These 5 lines along are mind blogging and complicated..

for i in range(remainder):
    key_list.append(key_list[i])

Key = ''.join(key_list)          #Till Here.

enc = []                        #contains the indexed text or symbol

for i in range(len(text)):
    if text[i] in Alpha:
        enc.append(Alpha[ Alpha.index(text[i]) + Alpha.index(Key[i].upper()) - len(Alpha) ])
    elif text[i] in alpha:
        enc.append(alpha[ alpha.index(text[i]) + alpha.index(Key[i].lower()) - len(alpha) ])
    else:
        enc.append(text[i])
    
enc_txt = ''.join(enc)

#                           ...END

print("\n Here's the encrypted text:- \n \n \t",enc_txt)
print("________________________________")
print("\n Copy, paste, Enjoy!")
