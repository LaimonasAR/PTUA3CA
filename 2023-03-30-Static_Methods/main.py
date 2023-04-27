# pylint: disable= missing-docstring


class Circle:
    ANOTHER_NAME = "Another Circle"

    def __init__(self) -> None:
        self.name = "Circle"

    def print_my_name(self):
        print(self.name)

    @staticmethod
    def print_another_name(name: str):
        print(name)


# 1
print(Circle.ANOTHER_NAME)
# 2
my_circle = Circle()
my_circle.print_my_name()
# 3
Circle.print_another_name("Laimonas")
