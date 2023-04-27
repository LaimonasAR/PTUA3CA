# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass
from typing import List

# class Position:
#     def __init__(self, name: str, lat: float, long: float) -> None:
#         self.name = name
#         self.lat = lat
#         self.long = long

# the same bellow


@dataclass
class Position:
    name: str
    lat: str
    long: str


pos = Position(name="Vilnius", lat=0.01, long=0.01)

print(pos.name, pos.lat, pos.long)


@dataclass
class Guest:
    name: str
    bill: float
    position: List[Position]

    def get_bill(self):
        return self.bill


first_guest = Guest(name="Vardenis", bill=0.01, position=pos)

print(first_guest.get_bill())
print(first_guest.get_bill())