def greater_than_100(x):
    return x > 100


print(list(filter(greater_than_100, [1, 111, 2, 222, 3, 333])))
# [111, 222, 333]
print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))


og_list = [
    42,
    "apple",
    True,
    3.14,
    None,
    ["cat", "dog", "bird"],
    {"name": "Alice", "age": 30},
    -17,
    "banana",
    False,
]

print(list(filter(lambda x: x.isdigit(), og_list))) #???
