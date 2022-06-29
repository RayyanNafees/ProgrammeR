
def factorial(num:int) -> int:
    """Returns the factorial(!) of the supplied integer."""
    if num < 0:
        raise TypeError("Negative numerals don't have Factorial")

    elif num == 0:
        factorial = 1

    else:
        factorial = 1
        for i in range(1,num+1):
            factorial = factorial*i

    return factorial
    
