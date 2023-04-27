# Lambda 1
print((lambda s: s.startswith("H"))("Hello World"))

# Lambda 2
print((lambda x, y: {1: x + 15, 2: x * y})(10, 15))

# Lambda 3
print(list(map(lambda x, y: x + y, [5, 6, 7], [5, 4, 3])))

# Lambda 4
print(list(map(lambda x: (x**2, x**3), [1, 2, 3, 4, 5, 6])))
# Lambda 5
print((lambda x: (x.split("-")))("2023-15-18 09:03:32.744178"))
