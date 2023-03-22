class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self) -> None:
        print(f"{self.name} MAKES LOUD SCREAMING, EEEEEEEEEEEEEEEEEEEEEEEE")


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        self.warm_blooded = warm_blooded
        self.name = name
        super().__init__(name=name)

    def give_birth(self):
        give_birth = "Can give birth"
        return give_birth


class Primate(Mammal):
    def __init__(self, name: str, opposable_thumbs: bool) -> None:
        self.opposable_thumbs = opposable_thumbs
        self.name = name
        super().__init__(name=name, warm_blooded=True)

    def can_swing(self):
        can_swing = "Can swing"
        return can_swing


my_primate = Primate("Antanas", True)

my_primate.make_noise()
