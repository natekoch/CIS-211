"""
Nate Koch 
CIS 211
Lab 7
"""

from typing import List, Callable, Dict
from math import sqrt

# Step 1
def total_sum(l: List[int]):
    total = 0
    for item in l:
        total += item
    return total

def apply(func: Callable, l: List[int]):
    new_l = []
    for i in range(len(l)):
        new_l.append(func(l[i]))
    return new_l
    
def square(l: List[int]):
    return apply(lambda x: pow(x, 2), l)

def magnitude(l: List[int]):
    return sqrt(total_sum(square(l)))

# Step 2
dispatch_table = {'sum': total_sum, 
                  'sqr': square, 
                  'mag': magnitude}

# Step 3
class FunctionDispatcher:

    def __init__(self, dict_funcs: Dict['key',Callable]):
        self.dict_funcs = dict_funcs

    def process_command(self, key: str, l: List[int]):
        return self.dict_funcs[key](l)

# Test
fd = FunctionDispatcher(dispatch_table)
print(fd.process_command('sum', [3,4])) # 7
print(fd.process_command('sqr', [3,4])) # [9, 16]
print(fd.process_command('mag', [3,4])) # 5.0