valid_moneys = (10, 50, 100, 500, 1000)

class Stock:
    juices = {}

    def __init__(self):
        # (price, number)
        self.juices["Coke"] = {"price": 120, "number": 5}

    def print_juices(self):
        for name, detail in self.juices.items():
            print(f"{name}: {detail['price']}yen, {detail['number']}hon")

class VendingMachine:
    total = 0
    stock = Stock()

    def refund(self):
        print(f"change: {self.total}")
        self.total = 0

    def is_valid(self, inserted):
        return inserted in valid_moneys

    def insert_or_refund(self):
        input_str = input("お金を入れてね、払い戻ししたい時はrefundと入力してね:")
        if input_str == "refund":
            self.refund()
        elif input_str == "stock":
            self.stock.print_juices()
        else:
            inserted = int(input_str)
            if self.is_valid(inserted):
                self.total += inserted
            else:
                print(f"change: {inserted}")
        print(f"total: {self.total}")


def main():
    vending_machine = VendingMachine()
    while True:
        vending_machine.insert_or_refund()
    
if __name__ == "__main__":
    main()
