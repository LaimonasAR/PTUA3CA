# 1

og_list = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]

# print(list(map(lambda x: x.sorted())))

print(sorted(og_list, key=lambda x: x[1]))

# 2

og_list = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

print(sorted(og_list, key=lambda x: x["color"]))

# 3

og_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

og_list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(sorted(og_list, key=lambda x: (x[0] + x[1] + x[2])))

print(sorted(og_list2, key=lambda x: (x[0] + x[1] + x[2])))
