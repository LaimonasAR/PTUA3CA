my_smth = {
    'Alpha': 1,
    'Beta': 2,
}

squares = {i * 5: i*i for i in range(10) if i <=6}
print(squares)

#create dict with 5 key: val; key - string, value -integer
names = {
    'Laimonas': 25,
    'Jonas': 34, 
    'Petras': 41, 
    'Bonifacijus': 15, 
    "Arnoldas": 5,
    }

my_dict = {name.upper(): int(str(number)[::-1]) for (name, number) in names.items()}
print(my_dict)

my_new_dict ={}
for name, number in names.items():
    my_new_dict[name.upper()] = int(str(number)[::-1])
    #           'Laimonas'               25   
    #           'LAIMONAS'               52    
    # my_new_dict["LAIMONAS"] = 52
print(my_new_dict)