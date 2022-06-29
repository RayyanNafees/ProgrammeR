
def Hash(text: object, algorithm: str) -> str:
    '''Returns the hashed-text of the supplied text, using the supplied algorithm.'''
    '''Supported algs = ['sha1', 'sha224', 'sha256', 'sha384', 'sha3_224',
                        'sha3_256', 'sha3_384', 'sha3_512', 'sha512']'''
    import hashlib

    keys  = ['sha1', 'sha224', 'sha256', 'sha384', 'sha3_224',
             'sha3_256', 'sha3_384', 'sha3_512', 'sha512']
    key = algorithm

    if key == 'sha2':    key = 'sha256'
    elif key == 'sha3':  key = 'sha384'
    elif key not in keys:key = 'sha1'

    enc = eval(f'hashlib.{key}')

    return enc(text.encode()).hexdigest()


def __make_eq(l: str, m: str) -> tuple:
    '''Returns a tuple of two strings of equal lengths.'''
    small, big = (l,m) if len(l) < len(m) else(m,l)
    small *= (a:=len(big)) // (b:=len(small))
    small += ''.join(small[i] for i in range(a%b))
    return (small,big) if small == l else (big,small)


def vigenere(text: str, key: str) -> str:
    text, key = __make_eq(text, key)
    Alpha = ''.join(chr(i) for i in range(65,65+26))
    alpha = Alpha.lower()
    a,A = alpha.index, Alpha.index
    return ''.join((alpha[a(t) + (a(k)-26)] if t in alpha else \
                    Alpha[A(t) + (A(k)-26)] if t in Alpha else t) for t,k in zip(text,key))

caeser = lambda text,key: ''.join(chr(ord(i) + int(key)) for i in text)

binary = lambda phrase, key: ' '.join(format(ord(x), 'b') for x in phrase)


morses= {'a' : '.-',
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
         '=' : '-...-' ,
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


morse = lambda text, key = None: ' '.join((morses[ch] if ch in morses else ch) for ch in text.lower().replace(' ','!:;'))


#_________________________________< decrypt >____________________________

uncaeser = lambda text,key: ''.join(chr(ord(i) - int(key)) for i in text)

unmorse = lambda morse_code: ''.join((opp_morse[code] if code in (opp_morse := {v : k for k,v in morses.items()})else code)
                                     for code in morse_code.split(' ')).replace('!:;',' ')

unbin = lambda bins: ''.join(chr(int(b, 2)) for b in bins.split(' '))

def devigenere(text: str, key: str) -> str:
    text, key = make_eq(text, key)
    Alpha = ''.join(chr(i) for i in range(65,65+26))
    alpha = Alpha.lower()
    a,A = alpha.index, Alpha.index
    return ''.join((alpha[a(t) - (a(k)-26)] if t in alpha else \
                    Alpha[A(t) - (A(k)-26)] if t in Alpha else t) for t,k in zip(text,key))