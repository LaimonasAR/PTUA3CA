my_list = [1,2,3,4,5,6,7,8,9]

number = my_list[0]
print(number)
for item in my_list[1:]:
    number = number * item

print(number)