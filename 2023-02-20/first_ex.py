# first_check = False
# second_check = False
# while first_check is False:
#     number_one = input("First number is: ")
#     try:
#         number_one = int(number_one)
#         first_check = True
#     except ValueError:
#         print("You must enter an integer")

from typing import Optional 

def first_func(number: int) -> Optional[int]:
    try:
        number = int(number)
        return number * number
    except ValueError:
        print("Value is not integer")
        
print(first_func(number = 5))

#--------------------------------

def second_func(number_one: int, number_two: int) -> None:
    try: 
        result = number_one / number_two
        print(result)
    except TypeError:
        print("type not integer")
second_func(number_one="a", number_two=5)

#---------------------------------

def third_func(number: int) -> None:

    try:
        number = 20 / number
        print(number)
    except ZeroDivisionError:
        print("do not divide by zero")
third_func(number=0)
#-----------------------------------

def fourth_func(name: str = "Laimonas") ->None:
    try:
        name[-4] = "Y"
        print(name)
    except Exception as e:
        print(f"Exception {e}")
fourth_func(name="H")

#------------------------------------

def fifth_func(name: str, surname: str) -> None:
    try: 
        full_name = name + surname
        print(Hello, world)
    except Exception as e:
        print(f"That was scary error - {e}")
    else:
        print(full_name)
fifth_func(name = "Laimonas", surname= "Paura")