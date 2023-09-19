# Задание 1. ** В классе Calculator создайте метод calculateDiscount,
# который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать
# исключение ArithmeticException. Не забудьте написать тесты для проверки этого поведения.

def calculate_discount(price: float, discount: float) -> float:
    if price <= 0:
        raise ArithmeticError("Стоимость покупки не может быть меньше нуля")
    if discount < 0:
        raise ArithmeticError("Размер скидки не может быть отрицательным числом")
    elif discount > 100:
        raise ArithmeticError("Скидка не может превышать 100 %")
    result = price - price * (discount / 100)
    return result


def price_amount():
    try:
        calculate_discount(0, 5)
        print('Что-то пошло не так')
    except ArithmeticError:
        print('Тест на сумму покупки успешно пройден')


def discount_amount_1():
    try:
        calculate_discount(500, -5)
        print('Что-то пошло не так')
    except ArithmeticError:
        print('Тест на отрицательную скидку успешно пройден')


def discount_amount_2():
    try:
        calculate_discount(500, 101)
        print('Что-то пошло не так')
    except ArithmeticError:
        print('Тест на размер скидки успешно пройден')


if __name__ == '__main__':
    price_amount()
    discount_amount_1()
    discount_amount_2()
