class Person:
    def __init__(self, name: str, surname: str) -> str:
        self.name = name
        self.surname = surname
    def greet(self):
        return f"Hello, my name is {self.name}"


person = Person("Laimonas", "Paura")
#print(person) #does nothing :)

print(person.name)

person2 = Person("Antanas", "Fontanas") 

print(person2.name)

print(person.greet())
print(person2.greet())
# class Hello:
#     def __init__(self, name: str) -> str:
#         self.name = name

