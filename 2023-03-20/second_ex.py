from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, currency: str, value: int) -> None:
        self.currency = currency
        self.value = value

    def get_value(self) -> int:
        return self.value

    def get_currency(self) -> str:
        return self.currency

    @abstractmethod
    def convert_to_currency(self, conversion_rate: float) -> float:
        pass


class Cash(Money):
    def __init__(self, currency: str, denomination: int) -> None:
        self.currency = currency
        self.value = denomination

    def convert_to_currency(self, conversion_rate: float) -> float:
        value = self.value * conversion_rate
        return value


class Card(Money):
    def __init__(self, currency: str, credit_limit: int) -> None:
        self.currency = currency
        self.value = credit_limit

    def convert_to_currency(self, conversion_rate: float) -> float:
        value = self.value * conversion_rate
        return value


my_cash = Cash(currency="Dollar", denomination=100)

my_card = Card(currency="Euro", credit_limit=1000)

print(my_card.convert_to_currency(1.5))

print(my_cash.convert_to_currency(1.2))
