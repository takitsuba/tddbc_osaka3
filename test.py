import unittest

from main import StockControl, VendingMachine

class TestStockControl(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = StockControl()
    
    def test_can_sell(self):
        self.assertEqual(self.sc.can_sell(120), True)
        self.assertEqual(self.sc.can_sell(0), False)

        # 本数が足りない時は販売できないことを確認する
        self.sc.stocks["Coke"] = 0
        self.assertEqual(self.sc.can_sell(120), False)
        

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


if __name__ == '__main__':
    unittest.main()
