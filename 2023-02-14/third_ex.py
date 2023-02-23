number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))

def calculations(num1: int, num2: int) ->list:
    calc_list = []

    my_sum = num1 + num2
    calc_list.append(my_sum)

    my_sub = num1 - num2
    calc_list.append(my_sub)

    my_mul = num1 * num2
    calc_list.append(my_mul)

    my_div = num1 / num2
    calc_list.append(my_div)

    return calc_list
result = calculations(number_one, number_two)
print(result)


#def calc_two(num1: int, num2: int) -> int:

