squares = []
for number in range(10):
    squares.append(number * number)
print(squares)

squares = [number * number for number in range(10)]
print(squares)