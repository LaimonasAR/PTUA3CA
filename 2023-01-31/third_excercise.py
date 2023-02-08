
first_check = False
second_check = False
while first_check is False:
    number_one = input("First number is: ")
    try:
        number_one = int(number_one)
        first_check = True
    except ValueError:
        print("You must enter an integer")



while second_check is False:
    number_two = input("Second number is: ")
    try:
        number_two = int(number_two)
        second_check = True
    except ValueError:
        print("You must enter an integer")

print(number_one * number_two)