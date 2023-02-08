#number = int(input("Enter number: "))
a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("AND condition")
# if a > b and a > c:
#     print("yesssssss")
# else:
#     print("nooooooo")

# print("OR condition")
# if a > b or a > c:
#     print("yesssssss")
# else:
#     print("nooooooo")

good_numbers = [1,5,9]

if a in good_numbers:
    if a == good_numbers[2]:
        print("You entered the last good number")
    else:    
        print("You entered good number, but not the last")
elif a == 21:
    print(f"Hey, it's {a}! ")
else:
    print("your number is not good")


