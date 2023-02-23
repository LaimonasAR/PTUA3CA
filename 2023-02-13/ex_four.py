text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

text_list = text.split(' ')

count_one = 0
for word in text_list:
    if len(word) > 5:
        count_one += 1
print(count_one)

count_two = 0

count_two = sum([count_two + 1 for i in text.split(' ') if len(i) > 5])
print(count_two)