class Car:
    total_cars_sold: int = 0

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        Car.total_cars_sold += 1

    @classmethod
    def get_total_cars_sold(cls) -> int:
        return cls.total_cars_sold


car1: Car = Car("Toyota", "Camry")

car2: Car = Car("Honda", "Civic")

print(Car.get_total_cars_sold())  # 2
