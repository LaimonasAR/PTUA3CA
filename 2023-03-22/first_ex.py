# write a function that accepts a number as a parameter.
#  The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.


def my_func(number: int):
    num_str = str(number)
    num_list = []
    for i in num_str:
        num_list.append(i)

    num_list.sort()
    new_list = []

    for i in num_list:
        new_list.append(i)

    num_one = int("".join(num_list))
    num_two = int("".join(new_list[::-1]))

    diff = num_two - num_one
    print(f"First number is {num_one}")
    print(f"Second number is {num_two}")
    print(f"Their difference is {diff}")


my_func(745826)
