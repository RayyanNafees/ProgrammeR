
def estimate(num: int, places: int) -> int:
    """Rounds off (estimates) the supplied interger to the nearest supllied decimal places."""
    """| Example: estimate(3456, 100) | estimate(3.1429, 0.01)"""
    """| Output: 3500 | 3.14"""

    if len(str(num)) >= len(str(places)) and places > 0:
        snum = str(num)
        splace = str(places)
        number = int(snum[len(snum) - len(splace)])

        number += 0 if number < 5 else 1
        place_num = len(snum)-len(splace)

        for i in snum[(place_num + 1):]:
            snum = snum.replace(i,'0')

        return int(snum)
    else:
        raise ArithmeticError(f'cannot estimate {num} to {places}th place.')
