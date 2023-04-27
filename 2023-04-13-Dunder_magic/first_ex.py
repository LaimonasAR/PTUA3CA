"""
Sukurkite klasę Product, kuri kaip parametrus priima pavadinimą ir kainą bei turi apibrėžtus __str__ ir __repr__ metodus.

    Metodas __str__ turėtų grąžinti eilutę formatu "Product: name, Price: price".
    Metodas __repr__ turėtų grąžinti eilutę formatu "Product('name', price)".
"""


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}"

    def __repr__(self) -> str:
        return f"Product {self.name, self.price}"


my_product = Product(name="Apple", price=2.56)

print(my_product)

print(repr(my_product))
