# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# itme1_price_total = item1_price * item1_quantity


class Item:
    def __init__(self, name, price, quantity ) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop",1000, 3)


print(item1.calculate_total_price(item1.price, item1.quantity))