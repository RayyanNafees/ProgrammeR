def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

hex_to_rgb("#ffffff")              # ==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")        # ==> (65535, 65535, 65535)
rgb_to_hex((255, 255, 255))        # ==> '#ffffff'
rgb_to_hex((65535, 65535, 65535))  # ==> '#ffffffffffff'

print('Please enter your colour hex')

_hex = input("")

print('Calculating...')
print(hex_to_rgb(_hex))
