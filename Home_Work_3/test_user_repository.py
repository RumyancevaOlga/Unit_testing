# Добавьте класс UserRepository для управления пользователями. В этот класс должен быть включен метод
# addUser, который добавляет пользователя в систему, если он прошел аутентификацию. Покройте тестами новую
# функциональность

import unittest
from user_repository import UserRepository
from user import User


class TestRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User("Peter", "I'm not spider-man")
        self.user_repository = UserRepository(self.user)

    def test_add_user(self):
        self.user.authenticate("Peter", "I'm not spider-man")
        self.user_repository.add_user()
        self.assertEqual(self.user_repository.list_user, [User("Peter", "I'm not spider-man")])
        self.user_repository.list_user.clear()

    def test_logout_user_is_not_admin(self):
        self.user.authenticate("Peter", "I'm not spider-man")
        self.user_repository.add_user()
        self.user_repository.logout()
        self.assertEqual(self.user_repository.list_user, [])
        self.user_repository.list_user.clear()

    def test_logout_user_is_admin(self):
        self.user.add_admin()
        self.user.authenticate("Peter", "I'm not spider-man")
        self.user_repository.add_user()
        self.user_repository.logout()
        self.assertEqual(self.user_repository.list_user, [User("Peter", "I'm not spider-man")])
        self.user_repository.list_user.clear()
