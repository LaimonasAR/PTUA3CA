"""Create three different tasks with real world scenario what would include 
all magic methods we covered today and plus 3 others from the provided list."""
from typing import List, Optional


class Dinner:
    def __init__(self, dishes: List[Optional[str]]) -> None:
        self.dishes = dishes

    def __str__(self) -> str:
        return "It's a dinner class"

    def __bool__(self) -> bool:
        if len(self.dishes) == 0:
            return False
        return True

    def __repr__(self) -> str:
        return f"Your healthy dinner consists of ({self.dishes})"

    def __add__(self, other: "Dinner") -> "Dinner":
        return Dinner(self.dishes + other.dishes)

    def __len__(self) -> int:
        return len(self.dishes)

    def __getitem__(self, item_nr: int) -> str:
        return self.dishes[item_nr]

    def __eq__(self, other: "Dinner") -> bool:
        if isinstance(other, Dinner):
            return self.dishes == other.dishes
        return False

    def __setitem__(self, index: int, item: str) -> None:
        self.dishes[index] = item



my_dinner = Dinner(["Soup", "Steak", "Cake"])
other_dinner = Dinner(["Soup", "Steak", "Cake"])
my_dinner_bonus = Dinner(["Beer", "Water"])
dinner = my_dinner + my_dinner_bonus

print(my_dinner)

print(f"Dinner exists? - {bool(my_dinner)}")

print(repr(my_dinner))

print(f"Menu with bonuses {dinner.dishes}")

print(f"Number of dishes in Your dinner is {len(my_dinner)}")

print(f"Second dish is {my_dinner[1]}")

print(f"Is Your dinner same as other peoples dinner? {my_dinner==other_dinner}")

my_dinner[1] = "Chicken"

print(repr(my_dinner))

