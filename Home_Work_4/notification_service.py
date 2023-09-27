class MessageService:

    def send_message(self, message: str, recipient: str) -> None:
        print(f'Сообщение {message} отправлено {recipient}')


class NotificationService:

    def __init__(self, message_service: MessageService):
        self._message_service = message_service

    @property
    def message_service(self):
        return self._message_service

    def sending_notification(self, message: str, recipient: str) -> None:
        self._message_service.send_message(message, recipient)
