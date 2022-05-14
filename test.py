import unittest

from main import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def setUp(self) -> None:
        self.vm = VendingMachine()

    def test_refund(self):
        self.vm.add_amount(100)

        self.vm.refund()
        self.assertEqual(self.vm.amount, 0)


if __name__ == '__main__':
    unittest.main()
