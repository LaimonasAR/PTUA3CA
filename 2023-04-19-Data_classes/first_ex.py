# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    ID: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_cost(self, number_of_items: Optional[int]) -> float:
        if number_of_items is None:
            return self.price * self.quantity_in_stock
        else:
            return self.price * number_of_items


product_one = Product(
    ID=1, name="Agurkas", description="Green", price=1.5, quantity_in_stock=15
)

print(product_one.calculate_cost(number_of_items=5))
print(product_one.calculate_cost(number_of_items=None))
