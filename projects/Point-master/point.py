class Point:

    def __init__(self, x: int, y: int):
        '''initializes a point object with x and y values'''
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        '''moves point to (x+dx, y+dy)'''
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        '''detirmines if two points have equal x and y values with the == operator'''
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self) -> str:
        '''returns a formated string (x, y)'''
        return f"({self.x}, {self.y})"

