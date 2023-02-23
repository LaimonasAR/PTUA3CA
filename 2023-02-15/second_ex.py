from typing import List, Tuple

def war_of_numbers(lst: List[int]) -> Tuple(str, int):
    '''Sums even and odd numbers in a list, returns winner name and int amount of points won by'''
    evens = 0
    odds = 0
    who_won = ""
    for value in lst:
        if value % 2 == 0:
            evens += value
        else:
            odds += value
    print(evens, odds)        
    if evens - odds > 0:
        who_won = "vens win by: "
        return who_won, evens - odds
    else:
        who_won = "Odds win by: "
        return who_won, odds - evens

winner, score = war_of_numbers([1,4,6,8,9,2,1,7,5,15,14])
print(winner, score)
