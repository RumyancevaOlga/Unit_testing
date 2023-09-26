# Разработайте и протестируйте метод numberInInterval, который проверяет,
# попадает ли переданное число в интервал (25;100).

import unittest
from number_in_interval import number_in_interval


class TestNumberInInterval(unittest.TestCase):

    def test_number_in_interval(self):
        self.assertEqual(number_in_interval(100), True)

    def test_number_is_not_in_interval(self):
        self.assertEqual(number_in_interval(101), False)
