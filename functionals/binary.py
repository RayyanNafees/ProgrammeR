
def binary(phrase: str) -> str:
    """Returns the binary numerals for the supplied phrase of characters."""
    return ' '.join(format(ord(x), 'b') for x in phrase)
