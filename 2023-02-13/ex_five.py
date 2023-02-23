import math

not_over = True

while not_over: 
    my_number = int(input("Enter your number: "))
    if my_number == 69:
        print("Joking already? I quit")
        not_over = False
    elif math.sqrt(my_number) == math.ceil(math.sqrt(my_number)):
        print(f"Your number {my_number} is indeed a perfect square")
    else:
        print(f"Sadly Your number {my_number} is not a perfect square ")
    