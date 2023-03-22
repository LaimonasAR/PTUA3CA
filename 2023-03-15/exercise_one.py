class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name: str, sides: int, width: float, height: float) -> None:
        self.name = name
        self.sides = sides
        self.width = width
        self.height = height
        Shape.__init__(self, name=name, sides=sides)

    def get_area(self):
        area = self.width * self.height
        return area


class Square(Rectangle):
    def __init__(self, side_lenght: float) -> None:
        self.side_lenght = side_lenght
        Rectangle.__init__(
            self, name="Square", sides=4, width=side_lenght, height=side_lenght
        )

        # Rectangle.__init__(name, sides, width, height)


my_square = Square(15)

print(my_square.get_area())
