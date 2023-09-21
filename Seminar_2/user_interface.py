import sys
from shop import Shop, Cart, Product

class UserInterface:
    def __init__(self, shop: Shop):
        self.shop = shop
        self.cart = Cart(self.shop)

    def _start_screen(self):
        print('Меню:\n'
              '1. Выбрать продукт\n'
              '2. Корзина\n'
              '0. Выход\n'
              'Ввод: ', end='')

    def _store_products_menu(self):
        print('Меню:\n'
              '1. Добавить товар в корзину\n'
              '2. Удалить товар из корзины\n'
              '0. Выход\n'
              'Ввод: ', end='')

    def _display_store_products(self):
        form = '{:>3}|{:<20}|{:<9}|{:<3}'
        print('В магазине доступны продукты:')
        print(form.format('ID', 'Название', 'Цена, р.', 'Количество в корзине, шт.'))
        for product in self.shop.products:
            print(form.format(product.id, product.title, product.cost, product.quantity))
        print()

    def _inner_choice(self):
        self._store_products_menu()
        user_choice = int(input())
        match user_choice:
            case 1:
                id_ = int(input('Введите ID продукта, который хотите добавить в корзину: '))
                self.cart.add_product_by_id(id_)
            case 2:
                id_ = int(input('Введите ID продукта, который хотите удалить: '))
                self.cart.remove_product_by_id(id_)

    def menu(self):
        while True:
            self._start_screen()
            user_choice = int(input())
            match user_choice:
                case 1:
                    self._display_store_products()
                    self._inner_choice()
                case 2:
                    self.cart.print_cart_items()
                case 0:
                    sys.exit()


if __name__ == '__main__':
    shop = Shop([Product(50, 'Milk', 1, 20)])
    user_interface = UserInterface(shop)
    user_interface.menu()
