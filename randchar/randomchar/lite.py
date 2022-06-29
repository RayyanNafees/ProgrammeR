
''' Lite & Faster way to generate random strings'''

from random import choice
from string import (
    ascii_letters as letters,
    ascii_lowercase as lowercase,
    ascii_uppercase as uppercase,
    octdigits,
    hexdigits,
    digits,
    punctuation,
)

joiner = lambda seq: lambda length=1: ''.join(choice(seq) for i in range(length-1))

letter =    joiner(letters)
lowerCase = joiner(lowercase)
upperCase = joiner(uppercase)
symbol =    joiner(punctuation)
printable = joiner(letters + digits + punctuation)


def digital(digs, isbyte = False): 
    def wrapper(self, length=1):
        prfx = '1' if isbyte else ''  # prefix if that's  Digit.binary()
        
        if length == 1:
            return choice(digs)
        else:
            return choice(digs[1:] +  prfx+''.join(choice(digs) for i in range(length - 1)))  if length > 1 else ''

    return wrapper



class Digit:
    '''
    The purpose of this class is to generate
    random digits in four number systems,
    '''
    binary = digital(digits[0:2], True)
    octal  = digital(octdigits)
    decimal= digital(digits) 

    hexadecimal=digital((hexdigits))
 

digit = Digit()  # an instance of the digit() class

user_set = lambda chars = '', length= 1: ''.join(choice(chars) for i in range(length)) if chars else ''

