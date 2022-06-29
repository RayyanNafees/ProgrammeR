
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

opp_morse = {v : k for k,v in morses.items()}            # To be used in 'unmorse' function.

def morse(text: str) -> str:
    '''Returns a morse code for the supplied text.'''
    text = str(text).lower().replace(' ','<>')

    enc = []
    for letter in text:
        if letter in morses:
            enc.append(morses[letter])
        else:
            enc.append(letter)

    return ' '.join(enc)


def unmorse(morse_code: str) -> str:
    '''Returns the original text from the supplied morse code.'''
    mlist = morse_code.split(' ')
    text = []

    for code in mlist:
        char = opp_morse[code] if code in opp_morse else code
        text.append(char)

    org_text = ''.join(text)
    return org_text.replace('<>',' ')
