"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixme:  We need a constructor, and __add__ method, and __eq__.
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vec") -> "Vec":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vec(new_x, new_y)

    def __eq__(self, other: "Vec") -> bool:
        """Equality operator """
        return (self.x == other.x) and (self.y == other.y)

class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self, pos: Vec, value: int):
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self.value = value

    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]: {self.value}"

    def __str__(self):
        return str(self.value)

    def __eq__(self, other: "Tile"):
        return self.value == other.value

    def move_to(self, new_pos: Vec):
        self.row = new_pos.x
        self.col = new_pos.y
        self.notify_all(GameEvent(EventKind.tile_updated, self))
    
    def merge(self, other: "Tile"):
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile.
        other.notify_all(GameEvent(EventKind.tile_removed, other))
    
class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = []  # a grid holds a matrix of tiles
        for row in range(rows):
            row_tiles = []
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)

    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]
    
    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

    def _empty_positions(self) -> List[Vec]:
        """Return a list of positions of None values, 
        i.e., unoccupied spaces."""
        empties = []
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                empties.append(Vec(row, col))
        return empties
            
    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is None:
                    return True
        return False
        # Should return True if there is some element with value None

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile 
        by its integer value and empty positions as 0"""
        result = []
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result

    def from_list(self, values: List[List[int]]):
        """Test scaffolding: set board tiles to the given
        values, where 0 represents an empty space."""
        for row in range(len(values)):
            for col in range(len(values[row])): 
                if values[row][col] == 0:
                    self.tiles[row][col] = None
                else:  
                    self.tiles[row][col] = Tile(Vec(row, col), values[row][col])     

    def place_tile(self, value=None):
        """Place a tile on a randomly chosen empty square."""
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = random.choice(empties)
        row, col = choice.x, choice.y
        if value is None:
            if random.random() < 0.1:
                value = 4
            else:
                value = 2
        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def in_bounds(self, pos: Vec) -> bool:
        """Is position (pos.x, pos.y) a legal position on the board?"""
        pos_x_in = (pos.x < self.rows) and (pos.x > -1)
        pos_y_in = (pos.y < self.cols) and (pos.y > -1)
        return pos_x_in and pos_y_in

    def slide(self, pos: Vec,  dir: Vec):
        """Slide tile at row,col (if any)
        in direction (dx,dy) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos

    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        tile = self.tiles[old_pos.x][old_pos.y]
        tile.move_to(new_pos)
        self.tiles[new_pos.x][new_pos.y] = tile
        self.tiles[old_pos.x][old_pos.y] = None

    def right(self):
        for row in range(len(self.tiles)-1, -1, -1):
            for col in range(len(self.tiles[row])-1, -1, -1):
                if self.tiles[row][col] is not None:
                    self.slide(Vec(row, col), Vec(0, 1))

    def left(self):
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is not None:
                    self.slide(Vec(row, col), Vec(0, -1))

    def up(self):
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is not None:
                    self.slide(Vec(row, col), Vec(-1, 0))

    def down(self):
        for row in range(len(self.tiles)-1, -1, -1):
            for col in range(len(self.tiles[row])-1, -1, -1):
                if self.tiles[row][col] is not None:
                    self.slide(Vec(row, col), Vec(1, 0))

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        values_list = self.to_list()
        total_score = 0
        for row in range(len(values_list)):
            total_score += sum(values_list[row])
        return total_score

