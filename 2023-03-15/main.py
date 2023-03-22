class Vehicle:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self):
        return self.name


class Engine:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hi_engine(self) -> None:
        print(f"Hi Engine with name {self.name}")


class Golfukas(Vehicle, Engine):
    def __init__(self, name: str, cost: float) -> None:
        super().__init__(name=name)
        Engine.__init__(self, name=name)
        self.cost: float = cost

    def get_cost(self) -> float:
        return self.cost


CAR_NAME = "Lieva tacka"
my_car = Golfukas(name=CAR_NAME, cost=100)

print(my_car.get_cost())
print(Golfukas.__mro__)


#OVER INHERITANCE PASIZIUREK

class Ferrari:

    def __init__(self, name: str) -> None:
        self.my_vehicle = Vehicle(name=name)


class Zapas:

    def __init__(self, my_vehicle: Vehicle) -> None:
        self.my_vehicle = my_vehicle

        

