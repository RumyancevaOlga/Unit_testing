# *Задание 2. (необязательное) *
# Мы хотим улучшить функциональность нашего интернет-магазина. Ваша задача - добавить два
# новых метода в класс Shop:
# Метод sortProductsByPrice(), который сортирует список продуктов по стоимости.
# Метод getMostExpensiveProduct(), который возвращает самый дорогой продукт.
# Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов
# (правильное количество продуктов, верное содержимое корзины).
# Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
# Напишите тесты для проверки корректности работы метода sortProductsByPrice
# (проверьте правильность сортировки). Используйте класс Product для создания экземпляров
# продуктов и класс Shop для написания методов сортировки и тестов.

from random import randint


class Product:

    def __init__(self, name, price: float = None):
        self.name = name
        if price is None:
            self.price = randint(10, 5000)
        else:
            self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return f'{self.name} = {self.price}'

    def __repr__(self):
        return f'Producr({self.name}, {self.price})'


class Shop:
    list_products = []

    def __init__(self, product: Product):
        self.product = Product
        Shop.list_products.append(product)

    def __str__(self):
        return f'{self.list_products}'

    def sort_product_by_price(self):
        return self.list_products.sort()

    def get_most_expensive_product(self):
        return max(self.list_products)


def testing_basket():
    product_1 = Product('milk', 50)
    product_2 = Product('cheese', 100)
    product_3 = Product('coffee', 75)
    shop = Shop(product_1)
    shop = Shop(product_2)
    shop = Shop(product_3)
    assert len(shop.list_products) == 3, 'Тест на количество продуктов в корзине провален'
    assert shop.list_products == [product_1, product_2, product_3], 'Тест на соответствие товаров в корзине провален'
    shop.list_products.clear()


def testing_get_most_expensive_product_method():
    product_1 = Product('milk', 50)
    product_2 = Product('cheese', 100)
    product_3 = Product('coffee', 75)
    shop = Shop(product_1)
    shop = Shop(product_2)
    shop = Shop(product_3)
    assert shop.get_most_expensive_product() == product_2, "Тест на самый дорогой продукт провален"
    shop.list_products.clear()


def testing_sort_product_by_price_method():
    product_1 = Product('milk', 50)
    product_2 = Product('cheese', 100)
    product_3 = Product('coffee', 75)
    shop = Shop(product_1)
    shop = Shop(product_2)
    shop = Shop(product_3)
    shop.sort_product_by_price()
    assert shop.list_products == [product_1, product_3, product_2], "Тест на сортировку пловален"
    shop.list_products.clear()


if __name__ == '__main__':
    testing_basket()
    testing_get_most_expensive_product_method()
    testing_sort_product_by_price_method()
