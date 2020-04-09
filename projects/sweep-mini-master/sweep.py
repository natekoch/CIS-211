"""
Nate Koch
CIS 211
List Sweep Algorithms
"""

def all_same(l: list) -> bool:
    same = True
    for i in range(len(l)):
        if l[0] != l[i]:
            same = False
            break
    return same

def dedup(l: list) -> list:
    deduped = []
    for item in l:
        if item not in deduped:
            deduped.append(item)
    return deduped

def max_run(l: list) -> int:
    max_run = 0
    current_run = 0
    if len(l) != 0: current_item_run = l[0]
    for i in range(len(l)):
        if l[i] == current_item_run:
            current_run += 1
        else:
            current_run = 1
            current_item_run = l[i]
        if current_run > max_run:
            max_run = current_run
    return max_run
        

