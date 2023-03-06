class Person:

    def __init__(self, name: str, surname: str) -> str:
        self.name = name
        self.surname = surname

    def full_name(self) -> str:
        f_name = f"{self.name} {self.surname}"
        return f_name

    def email(self)-> str:
        e_mail = (f"{self.name}.{self.surname}@company.com").lower()
        return e_mail
    
person = Person("Laimonas", "Paura")
print(person.email())
print(person.full_name())