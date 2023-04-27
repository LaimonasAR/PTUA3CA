
def f(x, y):
    return x + y


from functools import reduce
reduce(f, [1, 2, 3, 4, 5])
# 15 1+2, then +3, then + 4 then +5
