from unittest import TestCase
from sum_numbers import sum_numbers_multiple


class SumMultipleTest(TestCase):
    def test_multiple_3(self):
        result = sum_numbers_multiple(6)
        self.assertEqual(result, 8)
        result = sum_numbers_multiple(7)
        self.assertEqual(result, 14)

    def test_multiple_5(self):
        result = sum_numbers_multiple(10)
        self.assertEqual(result, 23)
        result = sum_numbers_multiple(11)
        self.assertEqual(result, 33)

    def test_multiple_3_n_5(self):
        result = sum_numbers_multiple(15)
        self.assertEqual(result, 45)
        result = sum_numbers_multiple(16)
        self.assertEqual(result, 60)

    def test_not_multiple(self):
        result = sum_numbers_multiple(2)
        self.assertEqual(result, 0)
        result = sum_numbers_multiple(3)
        self.assertEqual(result, 0)
