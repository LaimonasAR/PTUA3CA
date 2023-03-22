class Vehicle:
    def __init__(
        self, name: str, seats: int, vehicle_type: str, speed: int, consumption: float
    ) -> None:
        self.name = name
        self.seats = seats
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.consumption = consumption

    def get_name(self):
        return self.name

    def get_seats(self):
        return self.seats

    def get_fair_charge(self):
        charge = self.seats * 100
        if self.vehicle_type == "Bus":
            charge = charge * 1.1
        return charge

    def get_kilometers_per_liter(self):
        kpl = 100 / self.consumption
        return kpl

    def get_speed(self):
        return self.speed


class Bus(Vehicle):
    def __init__(self, name: str, seats: int) -> None:
        self.name = name
        self.seats = seats
        Vehicle.__init__(
            self, name=name, seats=seats, vehicle_type="Bus", speed=90, consumption=25
        )


class Taxi(Vehicle):
    def __init__(self, name: str, seats: int) -> None:
        self.name = name
        self.seats = seats
        Vehicle.__init__(
            self,
            name=name,
            seats=seats,
            vehicle_type="Taxi",
            speed=130,
            consumption=6.5,
        )


class Train(Vehicle):
    def __init__(self, name: str, seats: int) -> None:
        self.name = name
        self.seats = seats
        Vehicle.__init__(
            self,
            name=name,
            seats=seats,
            vehicle_type="Train",
            speed=300,
            consumption=1500,
        )


my_bus = Bus(name="Neoplan", seats=80)

print(my_bus.get_fair_charge())
my_taxi = Taxi(name="Ford", seats=4)

my_taxi.speed = 50
print(my_taxi.speed)
