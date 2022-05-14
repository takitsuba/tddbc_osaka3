import unittest

from main import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def test_refund(self):
        vm = VendingMachine()
        vm.add_amount(100)

        vm.refund()
        self.assertEqual(vm.amount, 0)

if __name__ == '__main__':
    unittest.main()
