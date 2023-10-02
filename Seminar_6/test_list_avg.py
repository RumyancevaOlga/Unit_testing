import pytest
from list_avg import find_average


def test_find_average():
    lst = [1, 2, 3, 4, 5]
    assert find_average(lst) == 3, 'test_find_average failed'


def test_empty_list():
    assert find_average([]) == 0.0, 'test_empty_list failed'


def test_find_average_not_num():
    lst = [1, 2, 3, 4, 'a']
    with pytest.raises(ValueError):
        assert find_average(lst)


def test_find_average_one_value():
    lst = [1]
    assert find_average(lst) == 1, 'test_find_average_one_value failed'


def test_find_average_not_list():
    lst = 3
    with pytest.raises(TypeError):
        find_average(lst)


if __name__ == '__main__':
    pytest.main(['-v'])
