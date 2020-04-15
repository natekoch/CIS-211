"""
Lab 3 - Shape3D

Author: Nate Koch
"""
from math import pi

class Shape3D:

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def print_info(self):
        print(f"Area: {self.area()} Volume: {self.volume()}")

class Cylinder(Shape3D):

    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        return pi * (self.radius ** 2) * self.height

    def area(self) -> float:
        return 2 * pi * (self.radius ** 2) + 2 * pi * self.radius * self.height

class Cuboid(Shape3D):

    def __init__(self, width: float, length: float, height: float):
        self.width = width
        self.length = length
        self.height = height

    def volume(self) -> float:
        return self.width * self.length * self.height

    def area(self) -> float:
        return 2 * self.width * self.length + 2 * self.width * self.height + 2 * self.length * self.height

class Cube(Cuboid):

    def __init__(self, width: float):
        self.width = width
        self.height = width
        self.length = width


cyl = Cylinder(3, 5)
cuboid = Cuboid(6,4,9)
lst = [Cube(3), cyl, cuboid]
for shape in lst:
    shape.print_info()

    
