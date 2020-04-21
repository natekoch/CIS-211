"""
Nate Koch
CIS 211
Lab 4
"""

from typing import List

class Node:

    def __init__(self, value: int):
        self.value = value

    def sum(self):
        raise NotImplementedError("Sum not yet implemented must create in concrete class")

    def __str__(self):
        return f"{self.value}"

class Internal(Node):

    def __init__(self, value: int, left: List[Node], right: List[Node]):
        self.value = value
        self.left = left
        self.right = right

    def sum(self) -> int:
        total = 0
        if isinstance(self.left, list):
            for node in self.left:
                total += node.sum()
        else:
            total += self.left.sum()
        if isinstance(self.right, list):
            for node in self.right:
                total += node.sum()
        else:
            total += self.right.sum()
        total += self.value
        return total

    def __str__(self) -> str:
        string = f"<{self.value}, {self.left.__str__()}, {self.right.__str__()}>"
        return string

class Leaf(Node):

    def __init__(self, value: int):
        self.value = value

    def sum(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.value}"

def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum())
    print(root)
    
if __name__ == '__main__':
    main()
