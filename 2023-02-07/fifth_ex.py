import random

my_number = random.randint(1,9)

#guessed_number = int(input("Guess the number: "))

num_check = False

i = 1

while not num_check:

    guessed_number = int(input("Guess the number: "))
  
    if my_number == guessed_number:
        if i == 1:
            print(f"Wow, first try is correct, it's {guessed_number}")
            num_check = True
        elif i == 2:
            print(f"You guessed right, it is {guessed_number} on the {i}-nd try")
            num_check = True
        elif i == 3:
            print(f"You guessed right, it is {guessed_number} on the {i}-rd try")
            num_check = True
        else:
            print(f"You guessed right, it is {guessed_number} on the {i}-th try")
            num_check = True
    else:
        print("Guess again")
        i = i + 1
