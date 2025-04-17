class Coin:
    def __init__(self, name, symbol, price, url, image_url):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.url = url
        self.image_url = image_url

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.price}"

    # equality
    def __eq__(self, other):
        return self.symbol == other.symbol

    # hash
    def __hash__(self):
        return hash(self.symbol)