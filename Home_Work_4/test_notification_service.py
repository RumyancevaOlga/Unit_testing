# Вам нужно написать тест с использованием моков для сервиса отправки сообщений.
# Условие: У вас есть класс MessageService с методом public void sendMessage(String message, String
# recipient), который отправляет сообщение получателю.
# Вам необходимо проверить правильность работы класса NotificationService, который использует
# MessageService для отправки уведомлений.


import unittest
from unittest.mock import Mock
from notification_service import NotificationService


class TestNotificationService(unittest.TestCase):

    def setUp(self) -> None:
        self.notification = NotificationService(Mock())

    def test_pay_calls_charge(self):
        self.notification.sending_notification('notification', 'client')
        self.notification.message_service.send_message.assert_called_once()
