name = input("Your name is: ")
age = input("Your age is: ")
age = int(age)
current_year = 2023
previuos_year = 2022
birth_year1 = current_year - age
birth_year2 = previuos_year - age
greeting = f"You were born in year {birth_year1} or {birth_year2}!"
print(greeting)
