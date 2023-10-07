# Создайте программу на Python или Java, которая принимает два списка чисел и выполняет
# следующие действия:
#  a. Рассчитывает среднее значение каждого списка.

class Average:

    def __init__(self, lst: list[int | float]):
        if not isinstance(lst, list):
            raise TypeError('Argument must be a list type')
        for item in lst:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} not int or float')
        self._lst = lst

    @property
    def lst(self):
        return self._lst

    def get_average(self) -> float:
        if len(self._lst):
            return sum(self._lst) / len(self._lst)
        return 0.0

    def __eq__(self, other):
        return self.get_average() == other.get_average()

    def __gt__(self, other):
        return self.get_average() > other.get_average()

    def __lt__(self, other):
        return self.get_average() < other.get_average()
