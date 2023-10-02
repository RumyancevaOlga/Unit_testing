# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - "Первый список имеет большее среднее значение", если среднее значение первого списка больше.
#  - "Второй список имеет большее среднее значение", если среднее значение второго списка больше.
#  - "Средние значения равны", если средние значения списков равны.
# ● Приложение должно быть написано в соответствии с принципами объектно-ориентированного
# программирования.

from average import Average


class CompareAverage:

    def __init__(self, average_1: Average, average_2: Average):
        self._average_1 = average_1
        self._average_2 = average_2

    @property
    def average_1(self):
        return self._average_1

    @property
    def average_2(self):
        return self._average_2

    def compare_average(self):
        if self._average_1 > self._average_2:
            return f"Первый список имеет большее среднее значение"
        elif self._average_1 < self._average_2:
            return f"Второй список имеет большее среднее значение"
        else:
            return f"Средние значения равны"
