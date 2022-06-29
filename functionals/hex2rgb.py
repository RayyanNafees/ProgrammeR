def hex2rgb(value: str) -> tuple:
    '''Returns the hexadecimal value from the supplied rgb color value.'''
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb2hex(rgb: tuple) -> str:
    '''Returns the rgb value from the supplied hexadecimal color value.'''
    return '#%02x%02x%02x' % rgb

rgb_to_hex = lambda rgb: '#%02x%02x%02x' % rgb


hex2rgb("#ffffff")              # ==> (255, 255, 255)
hex2rgb("#ffffffffffff")        # ==> (65535, 65535, 65535)
rgb2hex((255, 255, 255))        # ==> '#ffffff'
rgb_to_hex((65535, 65535, 65535))  # ==> '#ffffffffffff'
