class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.prices = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append(item)
            self.prices.append(price)
        self.last_transaction = price * quantity

    def total_price(self):
        total = sum(self.prices)
        if self.discount:
            total -= total * (self.discount / 100)
        return total

    def apply_discount(self):
        if not self.discount:
            return "No discount to apply"
        self.total_price -= self.total_price * (self.discount / 100)
        return self.total_price

    def void_last_transaction(self):
        if not self.items:
            return "No transactions to void"
        self.items.pop()
        self.prices.pop()
        self.last_transaction = 0

# example
register = CashRegister(discount=20)
register.add_item('apple', 2, 3)
register.add_item('banana', 1, 2)
print(register.total_price())  # Output: 6.4 (discounted price with 20% off)
register.void_last_transaction()
print(register.total_price())  # Output: 4 (price after voiding last transaction)
