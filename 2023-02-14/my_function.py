# def function_name():
#     print("Hello world!")

# function_name()

# a = 2
# b = 5


# def addition(number1, number2):
#     sum = number1 + number2
#     return(sum)


# c = addition(a, b)
# print(c)

# d = addition(50, 20)
# print(d)

# import random

# def get_random_number():
#     print(random.randint(0, 10))

# print(get_random_number())
# get_random_number()

# def find_sum(num1, num2):
#     '''Returns the sum of num1 and num2.''' #documentation
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# print(find_sum(5,9))

# find_sum(5,10)
# def even_or_not(number):
#     '''
#         Returns "even" if num is even, and "odd" if num is odd.    
#         Parameters:
#             num (int): Any integer    Returns:
#             type (string): "even" if num is even; "odd" if num is odd
    
#     '''
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(even_or_not(6))

def find_sum(num1, num2=50):
    '''Returns the sum of num1 and num2.'''
    sum_nums = num1 + num2  # Finds the sum of num1 and num2
    return sum_nums  # Returns the sum of the numbers

print(find_sum(5))
print(find_sum(5,10))

print(find_sum(num2=55, num1=4))


