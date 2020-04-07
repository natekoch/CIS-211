"""Classes and Subclasses"""

class Mammal:
    
    def hair_kind(self) -> str:
        return "Some kind of fur"
    
class Dog(Mammal):
    pass

fido = Dog()
print(fido.hair_kind())