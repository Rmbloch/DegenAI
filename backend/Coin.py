class Coin:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.price}"
