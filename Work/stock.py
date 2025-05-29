class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares*self.price

    def sell(self, nShares):
        self.shares -= nShares

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor*super().cost()



