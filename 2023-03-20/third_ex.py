from abc import ABC, abstractmethod


class Calculus(ABC):
    @abstractmethod
    def get_sum(self):
        pass

    @abstractmethod
    def get_diff(self):
        pass

    @abstractmethod
    def get_div(self):
        pass

    @abstractmethod
    def get_mult(self):
        pass

    def get_sqrt(self):
        pass


class Base(Calculus):
    def __init__(self, var_one: float, var_two: float) -> None:
        self.var_one = var_one
        self.var_two = var_two

    def get_sum(self) -> float:
        sum = self.var_one + self.var_two
        return sum

    def get_diff(self) -> float:
        diff = self.var_one - self.var_two
        return diff

    def get_div(self) -> float:
        division = self.var_one / self.var_two
        return division

    def get_mult(self) -> float:
        mult = self.var_one * self.var_two
        return mult

    def get_degr(self) -> float:
        degr = self.var_one**self.var_two
        return degr


class Geometry(Base):
    def __init__(self, sides: int, len_one: int, len_two: int) -> None:
        self.sides: int = sides
        self.var_one: float = len_one
        self.var_two: float = len_two
        super().__init__(self.var_one, self.var_two)

    def get_area(self) -> float:
        if self.sides == 3:
            area = super().get_mult() / 2
        if self.sides == 4:
            area = super().get_mult()
        return area

    def get_perimeter(self) -> float:
        perimeter = super().get_sum() * 2
        return perimeter


class Arithmetic(Base):
    def __init__(self, var_one: float, var_two: float) -> None:
        self.var_one: float = var_one
        self.var_two: float = var_two
        super().__init__(self.var_one, self.var_two)

    def calculations(self, operator: str):
        if operator == "+":
            result = super().get_sum()
        if operator == "-":
            result = super().get_diff()
        if operator == "/":
            result = super().get_div()
        if operator == "*":
            result = super().get_mult()
        if operator == "**":
            result = super().get_degr()
        return result


my_figure = Geometry(sides=4, len_one=5, len_two=6)

print(my_figure.get_area())
print(my_figure.get_perimeter())

my_calculation = Arithmetic(var_one=5, var_two=3)

print(my_calculation.calculations("**"))