# Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты,
# сквозные тесты) для этого приложения. Напишите название каждого теста, его тип и краткое описание того,
# что этот тест проверяет.


import unittest
from unittest.mock import Mock
from contact import Contact
from notebook import Notebook
from user_interface import UserInterface


class TestNotebook(unittest.TestCase):

    def setUp(self) -> None:
        self.notebook = Notebook()
        self.user_interface = UserInterface(Mock())
        self.user_interface_real = UserInterface(Notebook())

    # проверяем, что контакты корректно добавляются в записную книжку + contact_id
    # это юнит-тест, который проверяет работу функции add_contact
    def test_add_contact(self):
        self.notebook.add_contact(89265655445, 'Graph', 'Dracula')
        self.notebook.add_contact(89998887766, 'Bruce', 'Wayne')
        self.assertEqual(self.notebook.list_notebook,
                         [Contact(89265655445, 'Graph', 'Dracula', 1), Contact(89998887766, 'Bruce', 'Wayne', 2)])
        self.notebook.list_notebook.clear()

    # добавили контакт и удалили его же по id
    # это юнит-тест, который проверяет работу функции delete_contact_by_id
    def test_delete_contact_by_id(self):
        self.notebook.add_contact(89265655445, 'Graph', 'Dracula')
        self.notebook.delete_contact_by_id(1)
        self.assertEqual(self.notebook.list_notebook, [])
        self.notebook.list_notebook.clear()

    # проверяем, что при попытке удалить несуществующий контакт, выбрасывается исключение
    # это юнит-тест
    def test_delete_contact_by_no_id(self):
        self.assertRaisesRegex(RuntimeError, 'Не существует контакта с id = 1', self.notebook.delete_contact_by_id,
                               contact_id=1)

    # добавили контакт и изменили его же по id
    # это юнит-тест, который проверяет работу функции edit_contact_by_id
    def test_edit_contact_by_id(self):
        self.notebook.add_contact(89265655445, 'Graph', 'Dracula')
        self.notebook.edit_contact_by_id(1, 89998887766, 'Bruce', 'Wayne')
        self.assertEqual(self.notebook.list_notebook,
                         [Contact(89998887766, 'Bruce', 'Wayne', 1)])
        self.notebook.list_notebook.clear()

    # проверяем, что при попытке изменить несуществующий контакт, выбрасывается исключение
    # это юнит-тест
    def test_edit_contact_by_no_id(self):
        self.assertRaisesRegex(RuntimeError, 'Не существует контакта с id = 1', self.notebook.edit_contact_by_id,
                               contact_id=1, telephone=88888, name='Bruce')

    # проверили, что при добавлении контакта в пользовательском интерфейсе вызывается метод добавления в классе справочника
    # это интеграционный тест
    def test_user_interface(self):
        self.user_interface.add_contact(89998887766, 'Bruce', 'Wayne')
        self.user_interface.notebook.add_contact.assert_called_once()
        self.user_interface.notebook.list_notebook.clear()

    # проверяем, что при добавлении контакта через пользовательский интерфейс, данные записанные в записную книжку будут такими же
    # как и при добавлении контакта в непосредственно в класс записной книжки
    # это интеграционный тест
    def test_data_user_interface(self):
        self.user_interface_real.add_contact(89998887766, 'Bruce', 'Wayne')
        self.notebook.add_contact(89998887766, 'Bruce', 'Wayne')
        self.assertEqual(self.user_interface_real.notebook.list_notebook, self.notebook.list_notebook)
        self.user_interface.notebook.list_notebook.clear()
        self.notebook.list_notebook.clear()

    # тест проверяет данные в записной книжки после последовательных действий добавления, редактирования и удаления контактов
    # это сквозной тест
    def test_script_user_interface(self):
        self.user_interface_real.add_contact(89998887766, 'Bruce', 'Wayne')
        self.user_interface_real.add_contact(89265655445, 'Graph', 'Dracula')
        self.user_interface_real.edit_contact_by_id(2, 89265655445, 'Lord', 'Dracula')
        self.user_interface_real.delete_contact_by_id(1)
        self.assertEqual(self.user_interface_real.notebook.list_notebook, [Contact(89265655445, 'Lord', 'Dracula', 2)])
        self.user_interface.notebook.list_notebook.clear()


# Задание 2. Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест,
# интеграционный тест, сквозной тест) и объяснить, почему вы так решили.

# ● Проверка того, что функция addContact корректно добавляет новый контакт в список контактов".
# в моем примере это функция  def test_add_contact(self), которая является юнит-тестом, потому что проверяет работу одного модуля


# ● "Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно
# отображается в списке контактов".
# в моем примере это функция test_data_user_interface(self), которая является интеграционным тестом, поскольку проверяет правильность работы нескольких модулей в связке

# ● "Проверка полного цикла работы с контактом: создание контакта, его редактирование и
# последующее удаление".
# в моем примере это функция test_script_user_interface(self), которая является сквозным тестом, так как проверяет сценарий работы приложения

