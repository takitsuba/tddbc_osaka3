import unittest

from main import StockControl, VendingMachine


class TestStockControl(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = StockControl()

    def test_has_stock(self):
        juice = "Coke"
        self.assertEqual(self.sc.has_stock(juice), True)

        self.sc.stocks[juice] = 0
        self.assertEqual(self.sc.has_stock(juice), False)


class TestVendingMachine(unittest.TestCase):
    def setUp(self) -> None:
        self.vm = VendingMachine()

    def test_refund(self):
        self.vm.add_amount(100)

        self.vm.refund()
        self.assertEqual(self.vm.amount, 0)

    def test_is_valid(self):
        self.assertEqual(self.vm.is_valid(10), True)
        self.assertEqual(self.vm.is_valid(0), False)


if __name__ == "__main__":
    unittest.main()
