class Coffee_shop:
    def __init__(self, name: str, menu: list[dict], orders: list = []) -> None:
        self.name = name
        self.menu = menu
        self.orders = orders

