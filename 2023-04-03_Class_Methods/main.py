# class Calc:
#     My_NUMBER = 2

#     def __init__(self, nr: int) -> None:
#         Calc.My_NUMBER += nr



# cal_one = Calc(nr=3)

# print(cal_one.My_NUMBER)

# cal_two = Calc(nr=5)

# print(cal_two.My_NUMBER)
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    @classmethod
    def from_square(cls, side_length: float) -> 'Rectangle':
        return cls(side_length, side_length * 2)

rectangle1: Rectangle = Rectangle(3.0, 4.0)
rectangle2: Rectangle = Rectangle.from_square(2.0)

print(rectangle1.area())  # 12.0
print(rectangle2.area())  # 4.0