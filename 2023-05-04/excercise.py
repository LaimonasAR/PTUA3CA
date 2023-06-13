class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = value

    @property
    def farenheit(self) -> float:
        return (self.celsius * 1.8) + 32


my_temp = Temperature(15.5)
print(my_temp.farenheit)


my_temp.celsius = 20.5

print(my_temp.farenheit)
