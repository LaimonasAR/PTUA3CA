# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def get_name(self):
#         print(self.name)

#     @abstractmethod
#     def speak(self) -> None:
#         pass


# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def speak(self) -> None:
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


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self):
        print(self.name)

    def speak(self) -> None:
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print("Dog says Woof!")


class Cat(Animal):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print("Cat says Meow!")


my_dog = Dog("Rex")
my_cat = Cat("Felix")

my_dog.speak()
my_cat.speak()


my_dog.get_name()
my_cat.get_name()
