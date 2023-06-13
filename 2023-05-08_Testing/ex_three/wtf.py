def convert_portion(number):
    rom_number = ""
    if number == 0:
        rom_number = ""
    if number < 4 and number > 0:
        str = "I"
        for i in range(1, number):
            str = str + "I"
        rom_number = str
    if number == 4:
        rom_number = "IV"
    if number == 5:
        rom_number = "V"
    if number > 5 and number < 9:
        str = "I"
        for i in range(6, number):
            str = str + "I"
        rom_number = "V" + str
    if number == 9:
        rom_number = "IX"
    return rom_number


# print(convert_portion(0))
for i in range(0, 10):
    print(convert_portion(i))


# print(convert_portion(1))
