# squares = [number * number for number in range(10)]
# print(squares)

# squares = [number * number for number in range(10) if number != 5]
# print(squares)


names = ['Laimonas', 'Jonas', 'Petras', 'Bonifacijus', "Arnoldas"]

names_long = []
for name in names:
    if len(name) >= 7:
        names_long.append(name)
print(f'First list {names_long}')


names_long_two = [name for name in names if len(name) >= 7]
#names_long = [names for names in range(4) if len(names) >= 7]
print(f'Second list {names_long_two}')





