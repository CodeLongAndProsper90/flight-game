from random import randint
def generate():
    number = "0x"
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for i in range(0, 6):
        number = number + digits[randint(0, len(digits)-1)]
    return number


def make_darker(color):
    new_color = max(0, int(color, 0)-100)
    new_color = hex(new_color)
    return str(new_color)


def get_color_pair():
    hex_num = str(generate())
    dark_hex = make_darker(hex_num)
    hex_num = hex_num[2:].zfill(6)
    dark_hex = dark_hex[2:].zfill(6)

    hex_num = '#' + hex_num
    dark_hex = '#' + dark_hex

    return dark_hex, hex_num

