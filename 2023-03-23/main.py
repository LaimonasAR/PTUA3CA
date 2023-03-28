class Person:
    def __init__(self, name: str, age: str) -> None:
        self._name = name
        self.__age = age

    def get_name(self) ->str:   #taip reikt7 pasiimti jeo protected
        return self._name

    def get_age(self) ->str:    #taip reiktu pasiimti jei private
        return self.__age

me = Person(name="Laimonas", age=100)


print(me.get_name())
print(me.get_age())
