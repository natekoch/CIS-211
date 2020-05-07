"""
Nate Koch
Lab 6
"""

#exercise 1
'''
>>> a = 34
>>> bin(a)
'0b100010'
>>> b = 23
>>> bin(b)
'0b10111'
>>> a & b
2
>>> bin(a & b)
'0b10'
>>> a | b
55
>>> bin(a | b)
'0b110111'
>>> a >> 1
17
>>> a >> 2
8
>>> a >> 3
4
>>> b << 1
46
>>> b << 2
92
>>> b << 3
184
'''

#exercise 2
def extrac1_3(word: int) -> int:
    extracted = word & 0b00001110
    return extracted >> 1