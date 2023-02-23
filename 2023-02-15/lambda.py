#from typing import Callable

#def my_func(n: int) -> Callable:
def my_func(n: int):
    return lambda a: a ** n

my_doubler = my_func(2)

print(my_doubler(11))

my_doubler_two = my_func(11)(2)

print(my_doubler_two)