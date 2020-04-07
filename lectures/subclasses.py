"""Classes and Subclasses"""

class Mammal(object):
    """Mammal is an abstract base class"""
    
    def name(self) -> str:
        return self.animal_name
    
    def hair_kind(self) -> str:
        return "some kind of fur"

    def speak(self) -> str:
        return f"says {self.sound()}"

    def sound(self) -> str:
        raise NotImplementedError("Hey, sound was not defined")
    
class Dog(Mammal):

    def __init__(self, animal_name):
        self.animal_name = animal_name
    
    def milk_kind(self) -> str:
        return "dog milk"

    def hair_kind(self) -> str:
        return "dog hair"

    def sound(self) -> str:
        return "arf"

class Poodle(Dog):

    def __init__(self, animal_name):
        self.animal_name = animal_name

    def hair_kind(self) -> str:
        return f"{super().hair_kind()} Curly fur"

class Weasel(Mammal):

    def __init__(self, animal_name):
        self.animal_name = animal_name

    def sound(self) -> str:
        return "squeal"

fido = Dog("Fido")
fifi = Poodle("Fifi")
my_weasel = Weasel("Wesley")
my_pets = [fido, fifi, my_weasel]
for pet in my_pets:
    print(f"{pet.name()} has {pet.hair_kind()}")
    print(f"{pet.name()} {pet.speak()}")