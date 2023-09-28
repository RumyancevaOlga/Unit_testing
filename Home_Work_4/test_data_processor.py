# Вам требуется протестировать класс, который обрабатывает запросы к базе данных.
# Условие: У вас есть класс Database с методом public List<String> query(String sql), который выполняет SQLзапрос и возвращает результат.
# Вам необходимо проверить правильность работы класса DataProcessor, который использует Database для
# выполнения запроса и обработки результатов.

import unittest
from unittest.mock import patch
from data_processor import DataProcessor


class TestBook(unittest.TestCase):

    @patch('data_processor.DataProcessor')
    def test_book(self, mock_database):
        self.data_processor = DataProcessor(mock_database)
        sql = 'SELECT * FROM users'
        self.data_processor.request(sql)
        self.data_processor.database.query.assert_called_once_with(sql)
