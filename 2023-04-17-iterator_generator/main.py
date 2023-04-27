import time


def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num
        time.sleep(0.5)
        print(num)


# infinite_sequence()

my_generator = infinite_sequence()

# for value in my_generator:
#     print(value)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

# print(infinite_sequence())
