import pytest
from multiply import multiply


@pytest.mark.parametrize('a, b, result', [(10, 0, 0),
                                          (10, 1, 10),
                                          (10, -1, -10),
                                          (-10, -1, 10)])
def test_param_multiply(a, b, result):
    assert multiply(a, b) == result, 'test_param_multiply failed'


if __name__ == '__main__':
    pytest.main(['-v'])
