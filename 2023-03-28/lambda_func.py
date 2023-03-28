# reverse = lambda s: s[::-1]
# print(reverse("I am a string"))
# # 'gnirts a ma I'


# (lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)
# # 7.0
# (lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5)
# # 1.0

# print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))

# #--------------TAS PATS KAS -------------
# def kazkas(x1, x2, x3):
#     return (x1 + x2 + x3) / 3
# print(kazkas(9, 6, 6))

# # 7.0
# (lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5)
# # 1.0

# animals = ["ferret", "vole", "dog", "gecko"]


# def reverse_len(string: str) -> int:
#     return -len(string)


# print(sorted(animals, key=reverse_len))
# # ['ferret', 'gecko', 'vole', 'dog']

# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=lambda s: -len(s)))
# # ['ferret', 'gecko', 'vole', 'dog']


def func(x):
    return x, x**2, x**3


func(2)
# (2, 4, 16)
print((lambda x: (x, x**2, x**3))(2))  # Tuple
print((lambda x: [x, x**2, x**3])(2))  # List
print((lambda x: {x, x**2, x**3})(2))  # Set

print((lambda x: {1: x, 2: x**2, 3: x**3})(3))  #Dictionaryyyyyyyyyyyyy
