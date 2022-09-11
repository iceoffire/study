from enum import Enum
from typing import Tuple

class Direction(Enum):
    A_TO_B = 0
    B_TO_A = 1
    BOTH = 2

class Coordinate:
    def __init__(self, coord: Tuple, city: str):
        self.x = coord[0]
        self.y = coord[1]
        self.city = city

class Connection:
    def __init__(self, coord_a: Coordinate, coord_b: Coordinate, direction: Direction):
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.direction = direction
        self.distance = self.__calculate_distance(coord_a, coord_b)

    def __calculate_distance(self, coord_a, coord_b):
        delta_x = coord_b.x - coord_a.x
        delta_y = coord_b.y - coord_a.y
        return (delta_x**2 + delta_y**2)**0.5 # hypotenuse