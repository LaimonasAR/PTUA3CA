my_name = input("Enter Your name: ")
my_surname = input("Enter your surname: ")
my_age = input("Enter your age: ")

my_list = [my_name, my_surname, my_age]
my_keys = ["name", "surname", "age"]

my_dict = {}

for key, value in zip(my_keys, my_list):
    my_dict[key] = value

#print(my_dict)

age = 21

if int(my_dict["age"]) >= age:
    print("You are allowed to enter Casino")
else:
    print("You are not allowed to enter")
