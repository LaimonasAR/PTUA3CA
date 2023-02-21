# from typing import Any

# first_check = False
# second_check = False
# while first_check is False:
#     number_one = input("First number is: ")
#     try:
#         number_one = int(number_one)
#         first_check = True
#     except ValueError:
#         print("You must enter an integer")



# while second_check is False:
#     number_two = input("Second number is: ")
#     try:
#         number_two = int(number_two)
#         second_check = True
#     except ValueError:
#         print("You must enter an integer")

# print(number_one * number_two)

# from typing import Union

# def my_func(number: Union[float, int]) -> Union[float, int]:
#     return number / 2 if isinstance(number, float) else number // 2

# try:
#     my_div_number = my_func(0)
#     print(my_div_number)
#     #print(hello, world)
# except:
#     print("U f-ed up")


# try:
#     my_div_number = my_func(10)
#     print(my_div_number)
# except Exception as e:
#     print(f"Error : {e}")
# else:
#     #when no errors in try, do this
#     print("Success")



from typing import Union

def my_func(number: Union[float, int]) -> Union[float, int]:
    try:
        return number / 2 if isinstance(number, float) else number // 2
    except TypeError:
        print("wrong type")
    except Exception as e:
        print(f"Error : {e}")   
    else:
        return(number)
    finally:
        print("I am always printed") 
