import math


class Basic:
    def __init__(self, numb: int) -> None:
        self.numb = numb

    @classmethod
    def get_factorial(cls, numb: int) -> 'Basic':
        return math.factorial(numb)


print(Basic.get_factorial(8))

