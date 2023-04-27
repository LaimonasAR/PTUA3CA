"""1: Create a generator function that takes a positive integer n as input
 and generates all the even numbers up to and including n."""

from collections.abc import Iterator


def generator(n: int) -> Iterator[int]:
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
            # print(i)


my_even_numbers = generator(56)

for number in my_even_numbers:
    print(number)

# print(next(my_even_numbers))
# print(next(my_even_numbers))
# print(next(my_even_numbers))
# print(next(my_even_numbers))
# print(next(my_even_numbers))

# number = 56

# my_numbers_list = [i for i in range(1, number + 1) if i % 2 == 0]

# print(my_numbers_list)

# my_numbers_generator = (i for i in range(1, number + 1) if i % 2 == 0)

# print(next(my_numbers_generator))
# print(next(my_numbers_generator))
# print(next(my_numbers_generator))
# print(next(my_numbers_generator))
# print(next(my_numbers_generator))
