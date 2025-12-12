import unittest
from sum_numbers import sum_two_numbers

class TestSumTwoNumbers(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum_two_numbers(2, 3), 5)
    def test_sum_negative(self):
        self.assertEqual(sum_two_numbers(-2, -3), -5)
    def test_sum_mixed(self):
        self.assertEqual(sum_two_numbers(-2, 3), 1)
    def test_sum_zero(self):
        self.assertEqual(sum_two_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
