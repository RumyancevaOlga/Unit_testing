import unittest
from random_list import get_random_list
from max_num import  get_max_num


class TestRnd(unittest.TestCase):

    def test_rnd(self):
        lst = get_random_list(10)
        self.assertEqual(get_max_num(lst), sorted(lst)[-1])
        