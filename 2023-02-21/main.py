#from my_math import add, sub, prod, div
from shout import echo
import my_math as mt
#import random as rd

#print(__name__)
print(mt.add(1,5))

result = mt.prod(5,9)

print(result)

a = 5871684
b = 5584

res_two = mt.div(a,b)

print(res_two)

if __name__ == "__main__":
    print(f"this is {__name__}")

print(echo("Labas"))