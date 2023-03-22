from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> None:
        pass

    @abstractmethod
    def get_vehicle_cost(self) -> None:
        pass

    def get_error(self):
        raise NotImplementedError


class Car(Vehicle):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # super().__init__()
    def get_age(self):
        print(self.age)

    def get_name(self) -> None:
        print(self.name)

    def get_vehicle_cost(self) -> None:
        print("Too much")


my_car = Car(name="Audi", age=2018)

my_car.get_age()

my_car.get_vehicle_cost()
