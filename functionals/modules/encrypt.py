"""In Key,
•Enter an 'integer' for Caeser Cipher.
•Enter any 'word' for Vigenère Cipher.
•Enter any 'Hashing algorithm' like 'sha1 or md5 or sha384 etc.' for Hashing"""


def caeser(text: str, key: int) -> str:
    """Caeser ciphers the plain 'text' by using the supplied 'key'.
        In a caeser cipher,
        each character of the plain text is shifted by the provided int value.
        | Example: caeser_cipher('rayyan',-1)
        | Output: 'q`xx`m'
        Its typically based on ascii char set"""
    cipher = int(key)
    text_num = (ord(num) + cipher for num in text)

    return ''.join(chr(i) for i in text_num)


def Hash(text: object, algorithm: str) -> str:
    """Returns the hashed-text of the supplied text, using the supplied algorithm."""
    import hashlib

    key = str(algorithm)

    if key == 'sha1':     enc = hashlib.sha1
    elif key == 'sha256' or key == 'sha2': enc = hashlib.sha256
    elif key == 'sha224': enc = hashlib.sha224
    elif key == 'sha384': enc = hashlib.sha384
    elif key == 'md5':    enc = hashlib.md5
    elif key == 'sha512': enc = hashlib.sha512
    else: enc = hashlib.sha1

    return enc(text.encode()).hexdigest()


def vigenere(text: str, key: str) -> str:
    """Returns the Vigenère Ciphered text of the supplied text, using the provided key.
    Special characters and integers are not allowed as the 'key'.
    Special characters and integers in text are ignored while being encrypted.
    | Example: vigenere(Rayyan_Nafees+-931,rock).
    | Output: Ioairb_Xrtgoj+-931."""

    assert type(key) == str and type(text) == str, \
           "Text & Key must be an string !"

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in key:
        if char not in Alpha and char not in alpha:
            key.replace(char,'')

    key2 = key*(len(text)//len(key))
    remainder = len(text) % len(key)

    key_list = list(key2)            # These 5 lines along are mind blogging and complicated..

    for i in range(remainder):
        key_list.append(key_list[i])

    Key = ''.join(key_list)          # Till Here.

    enc = []                        # contains the indexed text or symbol

    for t,k in zip(text, Key):
        if t in Alpha:
            enc.append(Alpha[Alpha.index(t) + Alpha.index(k.upper()) - len(Alpha)])
        elif t in alpha:
            enc.append(alpha[alpha.index(t) + alpha.index(k.lower()) - len(alpha)])
        else:
            enc.append(t)

    return ''.join(enc)


def binary(phrase: str, key = None) -> str:
    """Returns the binary numerals for the supplied phrase of characters."""
    return ' '.join(format(ord(x), 'b') for x in phrase)


def morse(text: str, key = None) -> str:
    '''Returns a morse code for the supplied text.'''
    morses= {'a':'.-',
         'b' : '-...',
         'c' : '-.-.',
         'd' : '-..',
         'e' : '.',
         'f' : '..-.',
         'g' : '--.',
         'h' : '....',
         'i' : '..',
         'j' : '.---',
         'k' : '-.-',
         'k' : '-.-',
         'l' : '.-..',
         'm' : '--',
         'n' : '-.',
         'o' : '---',
         'p' : '.--.',
         'q' : '--.-',
         'r' : '.-.',
         's' : '...',
         't' : '-',
         'u' : '..-',
         'v' : '...-',
         'w' : '.--',
         'x' : '-..-',
         'y' : '-.--',
         'z' : '--..',
         '0' : '-----',
         '1' : '.----',
         '2' : '..---',
         '3' : '...--',
         '4' : '....-',
         '5' : '.....',
         '6' : '-....',
         '7' : '--...',
         '8' : '---..',
         '9' : '----.',
         '+' : '.-.-.',
         '-' : '-....-',
         '=' : '-...-',
         '_' : '..--.-',
         '!' : '-.-.--',
         '@' : '.--.-.',
         '$' : '...-..-',
         '/' : '-..-.',
         '(' : '-.--.',
         ')' : '-.--.-',
         "'" : '.----.',
         ':' : '---...',
         ';' : '-.-.-.',
         ',' : '--..--',
         '?' : '..--..'}

    text = str(text).lower().replace(' ','<>')

    enc = []
    for letter in text:
        if letter in morses:
            enc.append(morses[letter])
        else:
            enc.append(letter)

    return ' '.join(enc)
