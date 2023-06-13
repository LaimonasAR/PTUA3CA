"""rite python program that translates integer to roman. Try doing it in TDD style"""


# Symbols	Values
# I	1
# IV  	4
# V	5
# IX	9
# X	10
# XL	40
# L	50
# XC	90
# C	100
# CD	400
# D	500
# CM	900
# M	1000


class Roman:
    def __init__(self, number) -> None:
        self.number = number

    def divide(self):
        thousands = self.number // 1000
        hundreds = (self.number - (thousands * 1000)) // 100
        tens = (self.number - (thousands * 1000) - (hundreds * 100)) // 10
        singles = self.number - (thousands * 1000) - (hundreds * 100) - (tens * 10)
        
        return [thousands, hundreds, tens, singles]

    def convert(self):
        answer = ""
        div_number = self.divide()
        if div_number[1]:
            if div_number[1] >

        

    @staticmethod
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


my_number = Roman(1987)

# print(my_number.convert_portion(7))

print(my_number.divide())
