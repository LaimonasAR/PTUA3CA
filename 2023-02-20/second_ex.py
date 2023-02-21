from typing import Optional
def my_func(num_one: float, num_two: float) -> Optional[float]:
    try:
        result = num_one / num_two
       # return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Kinda Looks OK")
        return result * result
    finally:
        print("Well, one way or another I am here")

print(my_func(num_one=9, num_two=3))


    
