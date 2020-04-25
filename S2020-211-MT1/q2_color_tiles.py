"""Rows of tiles (Midterm problem)"""

import enum
from typing import List

class Color(enum.Enum):
    red = 1
    blue = 2

    def __str__(self) -> str:
        """'r' for red, 'b' for blue"""
        return self.name[0]

ABBREVIATIONS = { 'r': Color.red,
                  'b': Color.blue
                }

class Tile:
    """A single colored tile, either red or blue"""
    def __init__(self, tile_color: Color):
        self._color = tile_color

    def color(self) -> Color:
        return self._color

    def __eq__(self, other: "Tile") -> bool:
        """Tiles are equal if they have the same color"""
        if self.color() == other.color():
            return True
        else:
            return False

    def __str__(self) -> str:
        return str(self._color)

class Row:
    """A row of colored tiles"""
    def __init__(self):
        self.tiles = []

    def append(self, tile: Tile):
        self.tiles.append(tile)

    def __str__(self) -> str:
        str_rep = "" #string representation
        for tile in self.tiles:
            str_rep += str(tile)
        return str_rep

    def __eq__(self, other: "Row") -> bool:
        """Returns True only if the lengths are the 
        same and each tile has the same color"""
        length_same = len(self.tiles) == len(other.tiles)
        same_tiles = False
        if length_same:
            if len(self.tiles) == 0:
                same_tiles = True
            else:
                for i in range(len(self.tiles)):
                    if str(self.tiles[i]) != str(other.tiles[i]):
                        return False
                    else:
                        same_tiles = True
        return same_tiles

    def from_abbreviation(self, abbrv: str):
        """Converts a string abbreviation to a row of 
        tiles as specified by the string"""
        self.tiles = []
        for i in range(len(abbrv)):
            tile_color = abbrv[i]
            self.append(Tile(tile_color))

def main():
    row = Row()
    row.append(Tile(Color.blue))
    row.append(Tile(Color.red))
    row.append(Tile(Color.blue))

    print(row)

    row2 = Row()
    row2.from_abbreviation("brb")
    assert row == row2

if __name__ == "__main__":
    main()
