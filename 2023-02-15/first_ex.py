
from typing import List 

list_one = [1,2,3,4,5,6]

list_two = [6,5,4,3,2,1]

def compare(frst: List[int], scnd: List[int]) -> bool:
    '''Takes two lists, sums their values into third list, returns bool'''
    com_list = []
    equal = True
    if len(frst) == len(scnd):
        for  value1, value2 in zip(frst, scnd):
            com_list.append(value1 + value2)
#with comprehension - com_list = [sum(item) for item in zip(frsr, scnd)]
    else:
        equal = False
    if len(set(com_list)) != 1:
        equal = False

    return equal

result = compare(list_one,list_two)

print(result)


com_list = [sum(item) for item in zip(frsr, scnd)]