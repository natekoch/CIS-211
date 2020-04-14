"""Linked list - with recursion"""

class LinkedList:
    """Abstract base class"""
    def length(self) -> int:
        raise NotImplementedError("Needs length!")

class EmptyList(LinkedList):
    def length(self) -> int:
        return 0

class NonEmptyList(LinkedList):
    def __init__(self, word: str, tail: LinkedList):
        self.word = word
        self.tail = tail

    def length(self) -> int:
        return len(self.word) + self.tail.length()

x = EmptyList()
x = NonEmptyList("alpha", x)
x = NonEmptyList("beta", x)
x = NonEmptyList("gamma", x)
assert x.length() == 14
print(x.length())
    