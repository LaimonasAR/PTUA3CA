# my_number = 5


# def add(numb1: int, numb2: int) -> int:
#     return numb1 + numb2
#    #return numb1 + numb2 + my_number ------not good, not pure----------

# print(add(1, 2))

# my_number = 10

# print(add(1, 2))


# def say_hello() -> None:
#     print("hello")


# greet = say_hello

# greet()  # print 'hello'

from collections.abc import Callable


def say_hello(num1: int, num2: int) -> int:
    return num1 + num2


def another_function(f: Callable) -> None:
    my_number = 10
    my_number2 = 15
    return f(my_number, my_number2)


print(another_function(say_hello))


