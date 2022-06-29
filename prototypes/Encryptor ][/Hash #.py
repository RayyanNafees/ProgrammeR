import hashlib

text = input("Text: ")
key = str(input("Key: "))

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

hex_dig = hash_object.hexdigest()
print("\n Here's thehe encrypted text: \n \n \t",hex_dig) 
