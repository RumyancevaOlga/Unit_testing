import pytest
from average import Average
from compare_average import CompareAverage


# передаем несколько разных списков, проверяем результаты
@pytest.mark.parametrize('average_1, average_2, result',
                         [(Average([1, 2, 3]), Average([2, 3, 4]), 'Второй список имеет большее среднее значение'),
                          (Average([2, 3, 4]), Average([1, 2, 3]), 'Первый список имеет большее среднее значение'),
                          (Average([1, 2, 3]), Average([1, 2, 3]), 'Средние значения равны')])
def test_param_compare_average(average_1, average_2, result):
    assert CompareAverage(average_1, average_2).compare_average() == result, 'test_param_compare_average failed'


# проверяем свойства класса CompareAverage
def test_property_by_compare_average():
    average_1 = Average([1, 2, 3])
    average_2 = Average([2, 3, 4])
    comp = CompareAverage(average_1, average_2)
    assert comp.average_1 == Average([1, 2, 3]), 'test_property_by_compare_average failed'
    assert comp.average_2 == Average([2, 3, 4]), 'test_property_by_compare_average failed'


# проверяем правильность нахождения среднего значения списка
def test_find_average():
    lst = [1, 2, 3, 4, 5]
    assert Average(lst).get_average() == 3, 'test_find_average failed'


# проверяем правильность нахождения среднего значения при передаче пустого списка
def test_empty_list():
    assert Average([]).get_average() == 0.0, 'test_empty_list failed'


# проверяем отработку исключения при передачи в списоке НЕ числа
def test_find_average_not_num():
    lst = [1, 2, 3, 4, 'a']
    with pytest.raises(ValueError):
        assert Average(lst).get_average()


# проверяем правильность нахождения среднего значения при передаче списка из одного значения
def test_find_average_one_value():
    lst = [1]
    assert Average(lst).get_average() == 1, 'test_find_average_one_value failed'


# проверяем отработку исключения при передачи НЕ списка
def test_find_average_not_list():
    lst = 3
    with pytest.raises(TypeError):
        Average(lst).get_average()


if __name__ == '__main__':
    pytest.main(['-v'])
