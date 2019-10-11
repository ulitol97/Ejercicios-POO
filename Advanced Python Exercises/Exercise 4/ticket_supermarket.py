from datetime import datetime


class Ticket:
    """Docuaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
    def __init__(self, products=[]):
        self.products = products
        self.date = datetime.now()

    def compute_price(self):
        total = 0
        for p in self.products:
            total += p.price * p.amount

        return total


class Product:
    """Docuaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
    def __init__(self, price=1, amount=1):
        self.price = price
        self.amount = amount
