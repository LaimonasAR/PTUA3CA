text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

text_list = text.split(' ')

print(text_list)

how_many = 0

for e in text_list:
    if 'e' in e:
        how_many += 1
print(how_many)


count = 0
i = sum([count +1 for fff in text.split(' ') if "e" in fff])
print(i)