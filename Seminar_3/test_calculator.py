import unittest
from calculator import calculate_discount


class TestCalculator(unittest.TestCase):

    def test_purchase_exception(self):
        self.assertRaisesRegex(ValueError, 'Сумма не может быть меньше 0',
                               calculate_discount, purchase_amount=-7, discount_amount=5)

    def test_discount_less_zero_exception(self):
        self.assertRaisesRegex(ValueError, 'Скидка должна входить в диапазон от 0 до 100', calculate_discount,
                               purchase_amount=10, discount_amount=-1)

    def test_discount_more_hundred_exception(self):
        self.assertRaisesRegex(ValueError, 'Скидка должна входить в диапазон от 0 до 100', calculate_discount,
                               purchase_amount=10, discount_amount=101)

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)