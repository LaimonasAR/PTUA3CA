"""Create a generator function that would pick word from a generator and/list of generated random words 
(should be > 10000) and would stop itterating
until the word longer than 7 lettters is found.
Compare sizes of list and generator. 
Calculate performance per both executions (time to complete in ms)"""
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# from random_word import RandomWords
from py_random_words import RandomWords
from typing import List
from collections.abc import Iterator
import time


def random_word_list_compr(n: int) -> List[str]:
    rand_word_list = [RandomWords().get_word() for _ in range(n)]
    return rand_word_list


rand_words = random_word_list_compr(10000)

# print(rand_words)


def list_function_compr():
    # word_list = random_word_list_compr(10000)
    # for word in word_list:
    for word in rand_words:
        if len(word) < 12:
            continue
        else:
            print(f"Found long word {word}")
            break


start_time_ns = time.time_ns()
list_function_compr()
end_time_ns = time.time_ns()
timer_ns = end_time_ns - start_time_ns
print(f"List iteration time in nanoseconds -  {timer_ns}")


# def random_word_list(n: int) -> List[str]:
#     rand_word_list = []

#     for i in range(n):
#         word = RandomWords()
#         word = word.get_word()
#         rand_word_list.append(word)
#         i += 1
#     return rand_word_list


# def list_function():
#     word_list = random_word_list(10000)
#     for word in word_list:
#         if len(word) < 10:
#             continue
#         else:
#             print(f"Found long word {word}")
#             break


# start_time_ns = time.time_ns()
# list_function()
# end_time_ns = time.time_ns()
# timer_ns = end_time_ns - start_time_ns
# print(f"List creation with for loop and iteration time in nanoseconds -  {timer_ns}")


def random_word_generator(n: int) -> Iterator[str]:
    for i in range(n):
        word = RandomWords()
        word_gen = word.get_word()
        yield word_gen
        i += 1


def generator_function():
    word_gen = random_word_generator(100000)
    for word in word_gen:
        # for word in rand_words:
        if len(word) < 12:
            continue
        else:
            print(f"Found long word {word}")
            break


start_time_ns_g = time.time_ns()
generator_function()
end_time_ns_g = time.time_ns()
timer_ns_g = end_time_ns_g - start_time_ns_g
print(f"Generator time in nanoseconds -  {timer_ns_g}")
