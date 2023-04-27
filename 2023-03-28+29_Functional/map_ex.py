# 1

print(
    list(
        map(
            lambda x: x * 3,
            [
                1,
                2,
                5,
                8,
                4,
            ],
        )
    )
)

# 2

print(list(map(lambda x: x**2, [2, 6, 8, 5, 9, 7])))

# 3
print(list(map(lambda x, y, z: (x + y + z), [1, 2, 3], [4, 5, 6], [7, 8, 9])))

# 4
print(list(map(lambda x, y: (x + y), [1, 2, 3], [4, 5, 6])))
print(list(map(lambda x, y: (x - y), [1, 2, 3], [4, 5, 6])))
# 5

print(list(map(lambda x, y: (str(x) + str(y)), [1, 2, 3], (1, 2, 3))))

print(list(map(lambda x, y: (str(x) + " " + str(y)), [1, 2, 3], (1, 2, 3))))
