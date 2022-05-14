valid_moneys = (10, 50, 100, 500, 1000)

class StockControl:
    prices = {}
    stocks = {}

    def __init__(self):
        coke = "Coke"
        self.prices[coke] = 120
        self.stocks[coke] = 5

    def print_juices(self):
        for name in self.prices.keys():
            print(f"{name}: {self.prices[name]}yen, {self.stocks[name]}hon")

    def can_sell(self, amount):
        coke = "Coke"
        return self.prices[coke] <= amount and self.stocks[coke] > 0

    def take(self, name):
        self.stocks[name] -= 1


class VendingMachine:
    amount = 0
    proceeds = 0
    stock = StockControl()

    def refund(self):
        print(f"change: {self.amount}")
        self.amount = 0

    def is_valid(self, inserted):
        return inserted in valid_moneys

    def add_amount(self, inserted):
        self.amount += inserted

    def insert_or_refund(self):
        input_str = input("お金を入れてね、払い戻ししたい時はrefundと入力してね:")
        if input_str == "refund":
            self.refund()
        elif input_str == "stock":
            self.stock.print_juices()
        elif input_str == "buy":
            if self.stock.can_sell(self.amount):
                self.stock.take("Coke")
                price = self.stock.juices["Coke"]["price"]
                self.proceeds += price
                self.amount -= price
                print("buy: Coke")
        else:
            inserted = int(input_str)
            if self.is_valid(inserted):
                self.add_amount(inserted)
            else:
                print(f"change: {inserted}")
        print(f"total: {self.amount}")


def main():
    vending_machine = VendingMachine()
    while True:
        vending_machine.insert_or_refund()
    
if __name__ == "__main__":
    main()
