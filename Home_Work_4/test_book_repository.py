# У вас есть класс BookService, который использует интерфейс BookRepository для получения
# информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
# Mockito для создания мок-объекта BookRepository.


import unittest
from unittest.mock import Mock
from book_repository import BookService


class TestBookRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.book_service = BookService(Mock())

    def test_book_service(self):
        info = self.book_service.info('Алан Гарнер', 'Волшебный камень Бризингамена')
        self.assertEqual(info, 'Информация о книге "Волшебный камень Бризингамена" автора Алан Гарнер')
