

def first_number_input() -> float:
    check = False
    while check is False:
        number_one = input("First number is: ")
        try:
            number_one = int(number_one)
            check = True
            return number_one
        except ValueError:
            print("You must enter an integer")

def second_number_input() -> float:
    check = False
    while check is False:
        number_two = input("Second number is: ")
        try:
            number_two = int(number_two)
            check = True
            return number_two
        except ValueError:
            print("You must enter an integer")

def division(num_one: float, num_two: float) -> float:
    try:
        result= num_one / num_two
        return result
    except ZeroDivisionError as e:
        return e

print(first_number_input() * second_number_input())

