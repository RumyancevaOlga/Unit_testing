# Вам нужно написать тест с использованием моков для класса, который выполняет HTTP-запросы.
# Условие: У вас есть класс HttpClient с методом public String get(String url), который выполняет
# HTTP-запрос и возвращает результат. Вам необходимо проверить правильность работы класса
# WebService, который использует HttpClient для получения данных с веб-сайта.

import unittest
from unittest.mock import patch
from web_service import WebService


class TestWebService(unittest.TestCase):

    def setUp(self) -> None:
        with patch('web_service.WebService') as mock_web_service:
            self.web_service = WebService(mock_web_service)

    def test_web_service(self):
        url = 'https://gb.ru/'
        self.web_service.data(url)
        self.web_service.http_client.get.assert_called()
