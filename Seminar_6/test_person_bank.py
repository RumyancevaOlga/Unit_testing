import pytest
from bank import Bank
from person import Person
from unittest.mock import Mock


@pytest.fixture
def setup():
    bank = Bank()
    person = Person()
    person.add_money(100)
    return bank, person


def test_transfer_money(setup):
    bank, person = setup
    start_balance = bank.repo
    person.transfer_money(bank, 50)
    assert person.balance == 50, 'test_transfer_money failed'
    assert start_balance + 50 == 50, 'test_transfer_money failed'


def test_transfer_higher_money(setup):
    bank, person = setup
    # start_balance = bank.repo
    # person.transfer_money(bank, 150)
    # assert person.balance == 100, 'test_transfer_higher_money failed'
    # assert start_balance == 0, 'test_transfer_higher_money failed'
    with pytest.raises(ValueError):
        person.transfer_money(bank, 150)


def test_transfer_negative_money(setup):
    bank, person = setup
    with pytest.raises(ValueError):
        person.transfer_money(bank, -1)


def test_receive_money(setup):
    bank, person = setup
    bank = Mock()
    person.transfer_money(bank, 100)
    bank.receive_money.assert_called_with(100)


if __name__ == '__main__':
    pytest.main(['-v'])
