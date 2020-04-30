"""
Nate Koch
CIS 211
Lab 5
"""

from typing import List

class Node:

    def __init__(self, value: int):
        self.value = value

    def sum(self):
        raise NotImplementedError("Sum not yet implemented must create in concrete class")

    def __str__(self):
        return f"{self.value}"

    def copy(self):
        raise NotImplementedError("Copy not yet implemented must create in concrete class")

    def deepcopy(self):
        raise NotImplementedError("Deepcopy not yet implemented must create in concrete class")

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

    def copy(self) -> "Internal":
        return Internal(self.value, self.left, self.right)

    def deepcopy(self) -> "Internal":
        val = self.value
        
        left_side = []
        if isinstance(self.left, list): 
            for node in self.left:
                left_side.append(node.deepcopy())
        else: 
            left_side = self.left.deepcopy()

        right_side = []
        if isinstance(self.right, list):
            for node in self.right:
                right_side.append(node.deepcopy())
        else:
            right_side = self.right.deepcopy()

        return Internal(val, left_side, right_side)

class Leaf(Node):

    def __init__(self, value: int):
        self.value = value

    def sum(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.value}"

    def copy(self) -> "Leaf":
        return Leaf(self.value)

    def deepcopy(self) -> "Leaf":
        return Leaf(self.value)

def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    shallow = root.copy()
    deep = root.deepcopy()
    deep.right.value = 8
    print(deep) #<5, 3, <8, 6, 9>>
    print(root) #<5, 3, <7, 6, 9>>
    shallow.right.value = 8
    print(shallow) #<5, 3, <8, 6, 9>>
    print(root) #<5, 3, <8, 6, 9>>
    
if __name__ == '__main__':
    main()
