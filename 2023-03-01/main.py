class Smth:
    """This class is about Antanas, who is gone already"""

    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name #public, can be changed thorugh  my_name.name
        self._surname = surname #protected, can be accessed but not changed 
        self.__age = age # Cannot be accessed from outside
     

    def print_out_name(self):
        print(self.name, self._surname, self.__age)

    def change_name(self, name: str)-> None:
        print(self.__age)
        self.name = name
        
my_name = Smth(name="Antanas", surname="Baranauskas", age=25)

my_name.name = "Laimonas"

my_name.change_name(name="Jonas")

print(my_name.print_out_name())

# print(my_name.name)
# print(my_name._surname)
# print(my_name.__age)

# class Car:

#     def __init__(self, make_year: int, cost: float, color: str) -> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f"Full Car Info {make_year} - {cost} - {color}"
    
#     def get_car_color(self) -> None:
#         print(f"My car color: {self.color}")

#     def get_cost(self) -> float:
#         return self.cost

#     def get_full_info(self) -> None:
#         print(self.full_info)
class Car:

    def __init__(self, rand_num) -> None:   #calling Ferrari will overwrite this one 
        self._check_this_one: int = rand_num 
        self.__check_another_one: int = 2


    def get_car_color(self, color: str) -> None:
        print(f"My car color: {color}")

    def get_cost(self, cost: int) -> float:
        return cost

    def get_full_info(self, full_info: str) -> None:
        print(full_info)

class Ferrari(Car):
    # def __init__(self, hp: int) -> None:
    #     super().__init__()
    SPEED_CONSTANT = 20.5

    def __init__(self, hp: int, number: int) -> None:
        super().__init__(rand_num = number)
        self.hp = hp

    def get_max_speed(self)-> float:
        return self.hp * self.SPEED_CONSTANT
    
my_uber = Ferrari(hp=450, number = 555)
print(my_uber._check_this_one) #error
print(my_uber.get_max_speed())
