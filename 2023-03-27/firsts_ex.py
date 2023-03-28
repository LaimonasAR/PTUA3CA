class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def set_name(self) -> "Person":
        self.name = self.name.upper()
        return self

    def set_age(self) -> "Person":
        self.age = self.age
        return self


my_person = Person(name="Laimonas", age=105)

my_person.set_name().set_age()

print(f" Person is {my_person.name}, {my_person.age} years old")
#print(my_person.age)
