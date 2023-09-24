import unittest
from Vehicle import Car, Motorcycle, Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('VAZ', 'Lada Kalina', '2005')
        self.motorcycle = Motorcycle('Minsk', 'X250', '2020')

# Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof).
    def test_car_expands_vehicle(self):
        self.assertIsInstance(self.car, cls=Vehicle)

# Проверить, что объект Car создается с 4-мя колесами.
    def test_car_num_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

# Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_motorcycle_num_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

# Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def test_car_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

# Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive())
    def test_motorcycle_test_drive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

# Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    def test_car_parking(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

# Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
    def test_motorcycle_test_parking(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)
