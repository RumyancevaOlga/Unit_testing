# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли
# переданное число четным или нечетным

import unittest
from even_odd_number import even_odd_number


class TestEvenOddNumber(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(even_odd_number(4), True)

    def test_odd_number(self):
        self.assertEqual(even_odd_number(5), False)
