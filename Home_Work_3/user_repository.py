# Добавьте класс UserRepository для управления пользователями. В этот класс должен быть включен метод
# addUser, который добавляет пользователя в систему, если он прошел аутентификацию. Покройте тестами новую
# функциональность

from user import User


class UserRepository:
    list_user = []

    def __init__(self, user: User):
        self._user = user

    @property
    def user(self):
        return self._user

    def add_user(self):
        if self._user.is_authenticate:
            self.list_user.append(self._user)

    def __str__(self):
        return f'{self.list_user}'

# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей,
# кроме администраторов. Для этого, вам потребуется расширить класс User новым свойством,
# указывающим, обладает ли пользователь админскими правами. Протестируйте данную функцию.

    def logout(self):
        if not self._user.is_admin:
            self.list_user.remove(self._user)
