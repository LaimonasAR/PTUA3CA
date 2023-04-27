# pylint: disable= missing-docstring
from abc import ABC, abstractmethod


class ConversionTool(ABC):
    @abstractmethod
    def conversion_to_celsius(self, temp: float) -> float:
        pass

    @abstractmethod
    def conversion_to_farenheit(self):
        pass

    @abstractmethod
    def conversion_celsius_to_farenheit(self):
        pass


class Temperature(ConversionTool):
    @staticmethod
    def conversion_to_celsius(temp: float) -> float:
        temp_cels = temp - 273
        return temp_cels

    @staticmethod
    def conversion_to_farenheit(temp: float) -> float:
        temp_far = temp * (9 / 5) - 459.67
        return temp_far

    @staticmethod
    def conversion_celsius_to_farenheit(temp: float) -> float:
        temp_far = Temperature.conversion_to_celsius(temp) * 1.8 + 32
        return temp_far


kelvins = 300

print(
    f"{kelvins} degrees in Kelvins equals {Temperature.conversion_to_celsius(kelvins)} in Celsius"
)

print(
    f"{kelvins} degrees in Kelvins equals {round(Temperature.conversion_to_farenheit(300), 2)} in Fahrenheit"
)

print(
    f"{kelvins} degrees in Kelvins equals {Temperature.conversion_celsius_to_farenheit(300)} in Fahrenheit"
)
