animals = ["cat", "dog", "hedgehog", "gecko"]


def reverse(s):
    return s[::-1]


iterator = map(reverse, animals)
for i in iterator:
    print(i)
# tac
# god
# gohegdeh
# okceg

iterator = map(reverse, animals)
list(iterator)


animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(lambda s: s[::-1], animals)
list(iterator)
# ['tac', 'god', 'gohegdeh', 'okceg']

animals = ["cat", "dog", 5.5, "gecko"]
iterator = map(lambda s: str(s)[::-1], animals)
list(iterator)

list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))


def f(a, b, c):
    return a + b + c


print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))
# [111, 222, 333]
