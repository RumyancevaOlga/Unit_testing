import io
import unittest
from unittest.mock import patch

from shop import Shop, Product, Cart


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        product_names = ('bacon', 'beef', 'ham', 'salmon', 'carrot', 'potato', 'onion', 'apple', 'melon', 'rice', 'eggs', 'yogurt')
        product_prices = (170, 250, 200, 150, 15, 30, 20, 59, 88, 100, 80, 55)
        stock = (10, 3, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60)
        products = []
        for product_args in zip(product_prices, product_names, range(1, len(stock) + 1), stock):
            products.append(Product(*product_args))
        self.shop = Shop(products)
        self.cart = Cart(self.shop)

    def test_price_cart_is_correct_calculated(self):
        self.cart.add_product_by_id(1)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(1)
        self.assertEqual(self.cart.total_price, 790)

    def test_price_cart_products_same_type_is_correct_calculated(self):
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.assertEqual(self.cart.total_price, 700)

    def test_recalculation_after_remove_product_from_cart(self):
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(10)
        self.cart.remove_product_by_id(3)
        self.assertEqual(self.cart.total_price, 100)

    def test_changing_quantity_products_store(self):
        self.cart.add_product_by_id(1)
        self.assertEqual(self.shop.get_product_by_id(1).quantity, 9)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buying_last_store_product(self, mock_stdout):
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Этого товара нет в наличии')

    def test_return_product_in_shop_after_remove_from_cart(self):
        self.cart.add_product_by_id(1)
        self.cart.add_product_by_id(1)
        self.cart.remove_product_by_id(1)
        self.assertEqual(self.shop.get_product_by_id(1).quantity, 9)

    def test_select_incorrect_product_id_exception(self):
        self.assertRaisesRegex(RuntimeError, 'Продукт по номеру 20 не найден', self.cart.add_product_by_id, id_=20)

    def test_remove_products_from_cart_more_then_exist_exception(self):
        self.assertRaisesRegex(RuntimeError, 'Продукт по номеру 1 не найден', self.cart.remove_product_by_id, id_=1)
