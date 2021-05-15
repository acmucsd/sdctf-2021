# Generate flag for the list/array named a in this Desmos graph
# Rendered using Tupper's formula
# https://www.desmos.com/calculator/p6zpf4l36f

from typing import List, Union, Iterable
import font, sys

FONT = font.FONT_6x8

WIDTH = 6
HEIGHT = 8

# def rotate_left(n: int, nbit: int, bit_length: int):
#     assert 0 <= nbit <= bit_length
#     return rotate_right(n, bit_length - nbit, bit_length)

# def rotate_right(n: int, nbit: int, bit_length: int):
#     assert 0 <= nbit <= bit_length
#     mask = (1 << bit_length) - 1
#     return ((n << (bit_length - nbit)) & mask) | (n >> nbit)

def get_char_font(c: str):
    return get_codepoint_font(ord(c))

def get_codepoint_font(cp: int) -> List[int]:
    return FONT[HEIGHT * cp : HEIGHT * (cp + 1)]

def rotate_font_left(font_array: List[int]) -> List[int]:
    return list(map(lambda s: ((s << 1) & 0xff) | ((s & 0x80) >> (WIDTH - 1)), font_array))

def font2bitmap_num(font_array: List[int]) -> int:
    num = 0
    font_array = rotate_font_left(font_array)
    for i, row in enumerate(font_array):
        for j, bit in enumerate(bin(row)[2:].rjust(8, '0')):
            num += int(bit) << (HEIGHT * j + (HEIGHT - 1 - i))
    return num

# any character sequence (iterable of characters) is supported
def str_to_num_array(s: Iterable[str]) -> List[int]:
# def str_to_num_array(s: str) -> List[int]:
    return list(map(lambda c: font2bitmap_num(get_char_font(c)), s))

# Character-like type
C = Union[str, int]

def to_codepoint(c: C) -> int:
    return ord(c) if isinstance(c, str) else c

def get_desmos_font_array(start_char: C, end_char: C):
    start = to_codepoint(start_char)
    end = to_codepoint(end_char)
    return str_to_num_array(map(chr, range(start, end + 1)))

# print(font2bitmap_num(get_char_font('_')))
# print(str_to_num_array('pretty sick')) # [120831746623, 69258583586, 69426883100, 606239776, 606239776, 1007027513, 0, 17887275536, 46006272, 86472008220, 571738366]
# print(str_to_num_array('sdctf{f14g_1s_h3r3}'))
print(str_to_num_array(sys.argv[1]))

# print(get_desmos_font_array('0', '9'))
