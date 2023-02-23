from typing import List

my_addition = "'as"
names_list = ["Arnold", "John", "Bill"]
def add_str(my_list: List[str], my_string: str) -> list:
    i = 0
    for var in my_list:
        var = var + my_string
        my_list[i] = var
        i +=1
    return my_list

print(add_str(names_list, my_addition))

def add_str_two(my_lis: List[str], my_string: str) ->list:
    for count, value in enumerate(my_lis):
        my_lis[count] = value + my_string
    return my_lis

print(add_str_two(names_list, my_addition))