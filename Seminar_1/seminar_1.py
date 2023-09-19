from math import sqrt
from datetime import datetime


def square_root(num: float) -> float:
    if num < 0:
        raise RuntimeError(f'Число {num} должно быть положительным или равным 0')
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5, 'Тест с положительными числами провален'


def test_square_root_zero():
    assert square_root(0) == 0, 'Тест с нулевыми значениями провален'


def test_square_root_negative():
    try:
        square_root(-5)
    except RuntimeError:
        print('Все тесты прошли успешно')


def happy_new_year():
    current_date = datetime.now()
    assert current_date >= datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0), '2023 еще не наступил'


if __name__ == '__main__':
    # print(square_root(-10))
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()
    happy_new_year()

