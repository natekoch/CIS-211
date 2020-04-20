from typing import List

class Tree: 
    """Abstract base class"""

    def __init__(self):
        raise NotImplementedError("You can't do this")

    def count_nodes(self):
        """How many leaves in this tree?"""
        raise NotImplementedError("You forgot to implement me in subclass")

class Interior(Tree):

    def __init__(self, value: str, children: List[Tree]):
        self.value = value
        self.children = children

    def __str__(self) -> str:
        child_strs = [str(i) for i in self.children]
        children_str = ", ".join(child_strs)
        return f"{self.value}[{children_str}]"

    def count_nodes(self) -> int:
        """How many nodes does this interior subtree have?"""
        total = 1
        for child in self.children:
            total += child.count_nodes()
        return total



class Leaf(Tree):

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return f'"{self.value}"'

    def count_nodes(self) -> int:
        return 1

t = Interior("root", [Leaf("I'm a leaf"), Interior("interior", [Leaf("leaf1"), Leaf("leaf2")])])
print(t)
print(t.count_nodes())