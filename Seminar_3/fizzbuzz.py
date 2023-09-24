def fizz_buzz(num: int) -> str:
    assert type(num) == int, 'Ошибка типа данных. Ожидается тип int'
    if num % 15 == 0:
        return 'fizzbuzz'
    if num % 3 == 0:
        return 'fizz'
    if num % 5 == 0:
        return 'buzz'
    return str(num)
