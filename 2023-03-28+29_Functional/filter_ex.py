# 1

og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, og_list)))

print(list(filter(lambda x: x % 2 != 0, og_list)))

# 2

og_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), og_list)))


# 3

og_list = [1, 2, 3, 5, 7, 8, 9, 10]

print(len(list(filter(lambda x: x % 2 == 0, og_list))))

print(len(list(filter(lambda x: x % 2 != 0, og_list))))
