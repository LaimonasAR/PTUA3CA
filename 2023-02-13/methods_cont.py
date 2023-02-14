names = ['Laimonas', 'Jonas', 'Petras', 'Bonifacijus', "Arnoldas"]

my_dict = {}

for count, value in enumerate(names):
    my_dict[count] = value
print(my_dict)

my_dict_two = {poss: name for poss, name in enumerate(names)}
print(my_dict_two)