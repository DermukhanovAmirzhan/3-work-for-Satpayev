class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, name, price, quantity):
        self.items.append((name, price, quantity))
        self.total_price += price * quantity
