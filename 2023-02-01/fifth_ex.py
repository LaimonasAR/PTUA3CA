list_one = [1,2,3,4,5,6,7,8,9]
list_two = [9,8,7,6,5,4,3,2,1]

list_one.extend(list_two)
#list_one.append(list_two)
print(list_one)



list_one = [1,2,3,4,5,6,7,8,9]
list_two = [9,8,7,6,5,4,3,2,1]


list_three = []

my_index = 0
for item in list_one:
    #print(my_index)
    item = item + list_two[my_index]
    list_three.append(item)
    my_index = my_index + 1

print(list_three)