"""
Sukurkite klasę pavadinimu MyQueue, kurioje apibrėžti __bool__, __repr__ ir __len__ metodai.

    Metodas __bool__ turėtų grąžinti True, jei eilėje yra elementų, ir False, jei ji yra tuščia.
    Metodas __repr__ turėtų grąžinti eilutę formatu MyQueue(items), kur items yra eilės elementų sąrašas.
    Metodas __len__ turėtų grąžinti eilėje esančių elementų skaičių.
"""


class MyQueue:
    def __init__(self, queue: list) -> None:
        self.queue = queue

    def __bool__(self) -> bool:
        if len(self.queue) == 0:
            return False
        return True

    def __repr__(self) -> str:
        return f"MyQueue ({self.queue})"

    def __len__(self):
        return len(self.queue)


queue = MyQueue([1, 2, 3, 4, 5, 6])

print(bool(queue))

print(len(queue))

print(repr(queue))
