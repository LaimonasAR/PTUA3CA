from datetime import date



class Person:
    def __init__(self, name: str, surname: str) -> str:
        self.name = name
        self.surname = surname
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    def days_to_black_friday(self):
        today = date.today()
        bl_fr = date(
            year=2023,    # date.today(cls), #?????
            month=11,
            day=13,
        )
        ttl = bl_fr - today
        return ttl.days
    
    def get_eye_color(self, eye_color: str = "Brown") -> str:
        return eye_color 
    
    
        


person = Person("Laimonas", "Paura")
print(person.days_to_black_friday())
print(person.get_eye_color())
print(person.get_eye_color("Red"))
