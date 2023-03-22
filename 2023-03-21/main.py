import pdb


# class Animal:
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def get_name(self):
#         print(self.name)

#     def speak(self) -> None:
#         raise NotImplementedError


# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def speak(self) -> None:
#         pdb.set_trace()
#         print("Dog says Woof!")


# class Cat(Animal):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def speak(self) -> None:
#         print("Cat says Meow!")


# my_dog = Dog("Rex")
# my_cat = Cat("Felix")

# my_dog.speak()
# my_cat.speak()


# my_dog.get_name()
# my_cat.get_name()


# for i in range(1, 100):
#     i += 5
#     # pdb.set_trace()
#     print(i)

# import sys

# greeting = f"{sys.argv[1]} {sys.argv[2]}"
# print(greeting)
# args = {}
# i = 0
# while True:
#     argum = input("Enter Number ")
#     try:
#         arg = int(argum)
#     except ValueError:
#         print("not a number")
#         continue
#     args[i] = arg

#     i += 1
#     if i == 10:
#         break
# print(args)


import logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger("sLogger")

logger.debug("This is a debug message")
