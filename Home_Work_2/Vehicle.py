# В этом проекте, вы будете работать с проектом ""Vehicle"",
# который представляет собой иерархию классов, включающую абстрактный базовый класс ""Vehicle""
# и два его подкласса ""Car"" и ""Motorcycle"".
#
# Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"",
# а также поля ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".
#
# Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Car"",
# число колес устанавливается в 4, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 60,
# а в методе ""park()"" - обратно в 0.
#
# Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта
# ""Motorcycle"", число колес устанавливается в 2, а скорость в 0. В методе ""testDrive()""
# скорость устанавливается на 75, а в методе ""park()"" - обратно в 0.

import abc
import datetime


class Vehicle(abc.ABC):

    def __init__(self, company: str, model: str, year_release: datetime.date.year):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 0
        self._speed = 0

    def test_drive(self):
        pass

    def park(self):
        pass

    def __str__(self):
        return f'{self._company} {self._model} {self._year_release} {self._speed} {self._num_wheels}'


class Car(Vehicle):

    def __init__(self, company: str, model: str, year_release: datetime.date.year):
        super().__init__(company, model, year_release)
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 4
        self.speed = 0

    @property
    def num_wheels(self):
        return self._num_wheels

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0


class Motorcycle(Vehicle):

    def __init__(self, company: str, model: str, year_release: datetime.date.year):
        super().__init__(company, model, year_release)
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 2
        self.speed = 0

    @property
    def num_wheels(self):
        return self._num_wheels

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0
