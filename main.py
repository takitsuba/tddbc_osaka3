valid_moneys = (10, 50, 100, 500, 1000)


class StockControl:
    prices = {}
    stocks = {}

    def __init__(self):
        coke = "Coke"
        self.prices[coke] = 120
        self.stocks[coke] = 5

    def print_juices(self):
        for juice in self.prices.keys():
            print(f"{juice}: {self.prices[juice]}yen, {self.stocks[juice]}hon")

    def has_stock(self, juice):
        return self.stocks[juice] > 0

    def reduce_stock(self, juice):
        self.stocks[juice] -= 1


class VendingMachine:
    amount = 0
    proceeds = 0
    stock_control = StockControl()

    def refund(self):
        print(f"change: {self.amount}")
        self.amount = 0

    def is_valid(self, inserted):
        return inserted in valid_moneys

    def has_enough_amount(self, juice):
        return self.amount >= self.stock_control.prices[juice]

    def add_amount(self, inserted):
        self.amount += inserted

    def purchase(self, juice):
        if self.stock_control.has_stock(juice) and self.has_enough_amount(juice):
            self.stock_control.reduce_stock(juice)
            price = self.stock_control.prices[juice]
            self.proceeds += price
            self.amount -= price

    def insert_or_refund(self):
        input_str = input("お金を入れてね、払い戻ししたい時はrefundと入力してね:")
        if input_str == "refund":
            self.refund()
        elif input_str == "stock":
            self.stock_control.print_juices()
        elif input_str == "buy":
            juice = "Coke"
            self.purchase(juice)
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
